from django.urls import path
from . import views # the views file in the same app directory.

urlpatterns = [
    path('sunday', views.index), # the name of the function you made in views.
    path('monday', views.index) # the name of the function you made in views.
]