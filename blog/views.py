from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
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
        paginator = PageNumberPagination()
        paginator.page_size = 3
        results = paginator.paginate_queryset(posts, request)
        serialized_posts = PostSerializers(results, many=True).data
        return paginator.get_paginated_response(serialized_posts)
    except User.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)


class CustomPaginator(PageNumberPagination):
    page_size = 9


class PostListView(ListAPIView):
    """ get all Posts """
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    pagination_class = CustomPaginator


class PostDetailView(RetrieveAPIView):
    permission_classes = [IsAuthorOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializers
