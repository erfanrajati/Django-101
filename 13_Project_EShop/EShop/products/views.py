from django.shortcuts import render
from .models import Product

# Create your views here.

def products(request):
    products = Product.objects.all()
    return render(
        request, 
        'products/products.html', 
        context={'products':products}
    )

def product_details(request, dynamic):
    return render(request, 'products/product_details.html')