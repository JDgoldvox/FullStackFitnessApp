from typing import Any

from django.contrib.auth import authenticate
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware import csrf
from django.middleware.csrf import get_token

from rest_framework import status
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework.views import APIView, Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
    TokenVerifyView,
)
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from .serializers import CookieTokenVerifySerializer, CookieTokenRefreshSerializer

def get_tokens_for_user(user):
    if not user.is_active:
        raise AuthenticationFailed("User is not active")
    
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def setRefreshCookie(response: Response, token: str):
    response.set_cookie(
        key=settings.SIMPLE_JWT['REFRESH_AUTH_COOKIE'],
        value=token,
        expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
        secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
        httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
        samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
        path=settings.SIMPLE_JWT['REFRESH_TOKEN_PATH']
    )

def setAccessCookie(response: Response, token: str):
    response.set_cookie(
        key=settings.SIMPLE_JWT['AUTH_COOKIE'],
        value=token,
        expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
        secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
        httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
        samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
        # path=settings.SIMPLE_JWT['ACCESS_TOKEN_PATH']
    )

class AnonAuthRateThrottle(AnonRateThrottle):
    rate = '3/minute'

class CSRFTokenView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [AnonAuthRateThrottle]

    def get(self, request, format=None):
        return Response({settings.CSRF_COOKIE_NAME: get_token(request)})

class LoginView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [AnonAuthRateThrottle]

    @method_decorator(ensure_csrf_cookie)
    def post(self, request, format=None):
        data = request.data
        response = Response()
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)

        if user is not None:
            if not user.is_active:
                raise AuthenticationFailed("User is not active")
            else:
                data = get_tokens_for_user(user)
                # set cookies
                setRefreshCookie(response, data.pop('refresh'))
                setAccessCookie(response, data['access'])
                
                csrf.get_token(request)
                response.data = data
                response.status_code = status.HTTP_200_OK
                return response
        else:
            return Response({"detail": "Credentials are incorrect"}, status=status.HTTP_401_UNAUTHORIZED)

class CookieObtainPairView(TokenObtainPairView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            setRefreshCookie(response, response.data.pop('refresh'))
        if response.data.get('access'):
            setAccessCookie(response, response.data['access'])
        return super().finalize_response(request, response, *args, **kwargs)
    
class CookieTokenRefreshView(TokenRefreshView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            setRefreshCookie(response, response.data.pop('refresh'))
        if response.data.get('access'):
            setAccessCookie(response, response.data['access'])
        return super().finalize_response(request, response, *args, **kwargs)
    serializer_class = CookieTokenRefreshSerializer

class CookieTokenVerifyView(TokenVerifyView):
    serializer_class = CookieTokenVerifySerializer
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)