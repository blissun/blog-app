from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name="post_list"),
    path('@<str:username>/', views.get_user_posts, name="user_posts"),
    path('<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
    path('create/', views.PostCreateView, name="post_create"),
]
