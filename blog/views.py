from django.shortcuts import render
from django.views.generic import DetailView, ListView

from blog.models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
