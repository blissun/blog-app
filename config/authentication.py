from django.conf import settings
from django.core import exceptions
from rest_framework import authentication
import jwt
from rest_framework.exceptions import AuthenticationFailed

from users.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            baerer, jwt_token = token.split(' ')
            decoded_token = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = decoded_token.get('id')
            user = User.objects.get(pk=user_id)
            return user, None
        except ValueError or KeyError as e:
            print(e)
            return None
        except jwt.exceptions.DecodeError as e:
            print(e)
            raise AuthenticationFailed(detail="JWT Format Invalid")