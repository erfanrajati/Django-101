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

def product_details(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        raise Http404
    return render(
        request, 
        'products/product_details.html', 
        {'product':product}
    )