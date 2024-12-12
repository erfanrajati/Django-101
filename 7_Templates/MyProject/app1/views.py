from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.

def index(rquest):
    response = render_to_string("app1/index.html")
    return HttpResponse(response)
