from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model
from .forms import SignupForm
from .models import User
from django.utils.crypto import get_random_string
from django.urls import reverse


# Create your views here.
class UserView(View):
    def get(self, request):
        return render(request, 'user/dashboard.html', context={})

    def post(self, request):
        return render(request, 'user/dashboard.html', context={})
    
class SignupView(View):
    def get(self, request):
        signup_form = SignupForm()
        context = {
            "signup_form":signup_form
        }

        return render(request, 'user/signup.html', context)
    
    def post(self, request):
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            print(signup_form.cleaned_data)
            # redirect to dashboard
            user_email = signup_form.cleaned_data.get("email")
            # Check if email already exists
            user: User = User.objects.filter(email__iexact=user_email)
            if user: 
                signup_form.add_error('email', 'Email already exists')
            else: 
                new_user = User(
                    email=user_email, 
                    activation=get_random_string(48), # COOOOOOL!
                    username=user_email
                ) 
                new_user.set_password(signup_form.cleaned_data.get('password')) # a methdo coming from AbstractBaseUser
                new_user.save()
                # TODO: send activation code to user's email address

                return redirect(reverse("dashboard"))
                
        else:
            pass

        context = {
            "signup_form":signup_form
        }

        return render(request, 'user/signup.html', context)
