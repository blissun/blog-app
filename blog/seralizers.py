from rest_framework import serializers
from blog.models import Post
from users.models import User


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["pk", 'username', ]


class PostSerializers(serializers.ModelSerializer):
    author = TinyUserSerializer()

    class Meta:
        model = Post
        exclude = ()
