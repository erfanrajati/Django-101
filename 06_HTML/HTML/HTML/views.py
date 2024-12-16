from django.http import HttpResponse
from django.urls import reverse


def index(request):
    response = f"<h1>Hello, HTML!</h>"
    return HttpResponse(response)


def menu(request):
    m = {
        "Page_1": None,
        "Page_2": None,
        "Page_3": None,
    }

    dest = reverse("root", args=[])
    response = f"""
        <ul>
            <li> <a href="{dest}">Click Me!</a> </li>
        </ul>
    """
    
    return HttpResponse(response)