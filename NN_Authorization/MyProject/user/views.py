from django.shortcuts import render
from django.views import View


# Create your views here.
class UserView(View):
    def get(self, request):
        return render(request, 'user/dashboard.html', context={})