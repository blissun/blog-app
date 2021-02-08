from django.conf import settings
from django.core import exceptions
from rest_framework import authentication
import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import WrappedAttributeError

from users.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION')
            if token is None:
                return None
            baerer, jwt_token = token.split(' ')
            if baerer is not "Bearer":
                decoded_token = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
                user_id = decoded_token.get('id')
                user = User.objects.get(pk=user_id)
                return user, None
        except (ValueError, WrappedAttributeError, KeyError):
            return None
        except jwt.exceptions.DecodeError as e:
            print(e)
            raise AuthenticationFailed(detail="JWT Format Invalid")
