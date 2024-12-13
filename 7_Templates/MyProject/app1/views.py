from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.

def index(rquest):
    response = render_to_string("app1/index.html")
    return HttpResponse(response)

def r_index(request):
    data: dict = {
        'name':'Erfan',
        'family':'Rajati'
    }
    return render(request, "app1/render_index.html", context=data)
