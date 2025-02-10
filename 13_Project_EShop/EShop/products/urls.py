from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<dynamic>', views.product_details, name='product_details'),
]