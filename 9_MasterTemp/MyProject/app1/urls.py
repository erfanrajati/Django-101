from django.urls import path
from . import views

urlpatterns = [
    path("app1", views.index, name="app1"),
    path("<dynamic>", views.not_found, name="not_found")
]