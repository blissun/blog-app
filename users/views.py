import jwt
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import IsSelf
from users.serializers import UserSerializer, CreateUserSerializer


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == "list":
            permission_classes = [IsAdminUser]
        elif self.action == "create" or self.action == "retrieve":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsSelf]
        return [permission() for permission in permission_classes]

    def list(self, request):
        """ Only Admin User Access """
        return super().list(request)

    def update(self, request):
        """ Allow Is Self """
        return super().retrieve(request)

    @action(detail=False, methods=["post"])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user is not None:
            encoded_jwt = jwt.encode({"id": user.id}, settings.SECRET_KEY, algorithm="HS256")
            return Response(data={'token': encoded_jwt, 'id': user.id})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
