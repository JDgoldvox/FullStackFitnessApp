from typing import Any

from django.contrib.auth import authenticate
from django.conf import settings

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework.views import APIView, Response
from rest_framework.throttling import AnonRateThrottle
from django.middleware import csrf

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import InvalidToken


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
        samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
    )

class AuthRateThrottle(AnonRateThrottle):
    rate = '3/minute'

class LoginView(APIView):
    throttle_classes = [AuthRateThrottle]

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

class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None
    def validate(self, attrs: dict[str, Any]) -> dict[str, str]:
        attrs['refresh'] = self.context['request'].COOKIES.get(settings.SIMPLE_JWT['REFRESH_AUTH_COOKIE'])
        if attrs['refresh']:
            return super().validate(attrs)
        else:
            raise InvalidToken("refresh token and/or access token not found")

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