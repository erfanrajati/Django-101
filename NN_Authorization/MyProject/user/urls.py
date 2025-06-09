from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserView.as_view(), name='dashboard'),
    path('signup', views.SignupView.as_view(), name='signup'),
]