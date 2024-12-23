from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="main"),
    path("posts", views.posts, name="posts"),
    path("posts/<slug:slug>", views.single_post, name="post_details"), # mywebsite.com/post/new-post
]