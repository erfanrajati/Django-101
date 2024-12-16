from django.http import HttpResponse

def dynamic_view(request, dynamic, dynamic2, dynamic3):
    return HttpResponse((dynamic, dynamic2, dynamic3))