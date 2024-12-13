from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    data = {
        "HoHoHo": ["Santa", "Christmas", "Candy"] # Yes my child it's Christmas at the time I'm writing this!
    }
    return render(request, "app1/index.html", context=data)