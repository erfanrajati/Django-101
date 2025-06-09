from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

class SignupForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(),
        validators=[
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput()
    )
    password_confirm = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput()
    )

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password == password_confirm:
            return password_confirm
        else:
            raise ValidationError("Passwords don't match! Try again fuck face.")