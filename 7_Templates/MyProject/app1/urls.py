from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app1'),
    path('rendered/', views.r_index, name='app1_rendered')
]