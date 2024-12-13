from django.http import HttpResponseRedirect
from django.urls import reverse

def redirect(request):
    return HttpResponseRedirect(reverse('app1_rendered', args=[]))