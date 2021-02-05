from django.shortcuts import render
from django.views.generic import DetailView, ListView
from rest_framework.generics import ListAPIView, RetrieveAPIView

from blog.models import Post
from blog.permissions import IsAuthorOnly
from blog.seralizers import PostSerializers


class PostListView(ListAPIView):
    """ get user Posts """
    serializer_class = PostSerializers

    def get_queryset(self):
        user = self.request.user
        queryset = Post.objects.filter(author=user)
        return queryset


class PostDetailView(RetrieveAPIView):
    permission_classes = [IsAuthorOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializers
