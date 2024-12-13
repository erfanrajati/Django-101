from django.urls import path
from . import views

urlpatterns = [
    path('2025/', views.index)
]