from django.shortcuts import render
from .models import Product
from django.http import Http404

# Create your views here.

def products(request):
    products = Product.objects.all()
    return render(
        request, 
        'products/products.html', 
        context={'products':products}
    )

def product_details(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except:
        raise Http404
    return render(
        request, 
        'products/product_details.html', 
        {'product':product}
    )