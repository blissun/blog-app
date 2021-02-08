from rest_framework import serializers
from blog.models import Post
from users.models import User
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["pk", 'username', ]


class PostSerializers(serializers.ModelSerializer):
    author = TinyUserSerializer()
    tags = TagListSerializerField()

    class Meta:
        model = Post
        exclude = ()


class WriteSerializers(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = (
            "title", "content", "tags"
        )

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        instance = Post.objects.create(**validated_data)
        instance.tags.set(*tags)
        return instance
