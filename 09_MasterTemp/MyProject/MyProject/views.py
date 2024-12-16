from django.http import HttpResponseRedirect
from django.urls import reverse

def redirect_to_app1(request):
    return HttpResponseRedirect(reverse("app1"))