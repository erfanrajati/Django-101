from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request): # or any name you want
    return HttpResponse("Hello, World!")
