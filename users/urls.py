from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.UsersView.as_view()),
    path("login/", views.login),
    path("me/", views.MeView.as_view()),
    path("@<str:username>/", views.user_detail),
]