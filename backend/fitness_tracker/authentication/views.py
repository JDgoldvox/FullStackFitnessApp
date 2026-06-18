from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings
# from .models import *

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework.views import APIView, Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django.middleware import csrf


def get_tokens_for_user(user):
    if not user.is_active:
        raise AuthenticationFailed("User is not active")
    
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

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
                response.set_cookie(
                    key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                    value=data['access'],
                    expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                csrf.get_token(request)
                response.data = data
                response.status_code = status.HTTP_200_OK
                return response
        else:
            return Response({"detail": "Credentials are incorrect"}, status=status.HTTP_401_UNAUTHORIZED)
