from typing import Any

from django.conf import settings

from rest_framework import status
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenVerifySerializer, TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

class CookieTokenVerifySerializer(TokenVerifySerializer):
    token = serializers.CharField(required=False, allow_blank=True)

    def validate(self, attrs: dict[str, None]) -> dict[Any, Any]:
        request: Request = self.context.get('request') # type: ignore
        if request is None or not request:
            raise ValidationError({"detail": "request missing context"})
        cookie_name = settings.SIMPLE_JWT['AUTH_COOKIE']
        if 'token-type' in request.data: # type: ignore
            try:
                cookie_name = request.data['token-type'] + "_token" # type: ignore
                if "_token" not in cookie_name: cookie_name += "_token"
            except KeyError as e:
                raise ValidationError({
                    "token-type": "This is a required field"
                })
        token = request.COOKIES.get(cookie_name)

        if token is None:
            raise ValidationError({
                "detail": f"Cookie with name {cookie_name} was not found"
            })

        attrs['token'] = token # type: ignore
        return super().validate(attrs)

class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None
    def validate(self, attrs: dict[str, Any]) -> dict[str, str]:
        attrs['refresh'] = self.context['request'].COOKIES.get(settings.SIMPLE_JWT['REFRESH_AUTH_COOKIE'])
        if attrs['refresh']:
            return super().validate(attrs)
        else:
            raise InvalidToken("refresh token and/or access token not found")