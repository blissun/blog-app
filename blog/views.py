from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Post
from blog.permissions import IsAuthorOnly
from blog.seralizers import PostSerializers
from users.models import User


@api_view(["GET"])
def get_user_posts(request, username):
    try:
        user = User.objects.get(username=username)
        posts = Post.objects.filter(author=user.id)
        serialized_posts = PostSerializers(posts, many=True).data
        return Response(status=200, data=serialized_posts)
    except User.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)


class PostListView(ListAPIView):
    """ get all Posts """
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDetailView(RetrieveAPIView):
    permission_classes = [IsAuthorOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializers
