from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path("/<slug:slug>", views.post_details, name="post_details")
]