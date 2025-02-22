from django.shortcuts import render
from .models import Product
from django.http import Http404

# Create your views here.

def products(request):
    products = Product.objects.all().order_by('name')
    prod_count = products.count()
    return render(
        request, 
        'products/products.html', 
        context={
            'products':products,
            'prod_count':prod_count,
        }
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