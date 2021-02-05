from abc import ABC

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile_image",
        )
        read_only_fields = ("id",)


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ('password', 'password1', 'username')

    def validate_password(self, password):
        password1 = self._kwargs['data'].get('password1')
        if password == password1:
            return password
        else:
            raise serializers.ValidationError("Passwords do not match each other.")

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
            raise serializers.ValidationError("This username already exists.")
        except User.DoesNotExist:
            return username

    def create(self, validated_data):
        del validated_data['password1']
        password = validated_data['password']
        new_user = super().create(validated_data)
        new_user.set_password(password)
        new_user.save()
        return new_user
