from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound
# Create your views here.
def index(request):
    return render(request, "app1/index.html")


def not_found(request, dynamic):
    response = render_to_string('404.html')
    return HttpResponseNotFound(response)