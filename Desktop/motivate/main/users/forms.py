from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control form-control-user",
                "placeholder": "Username"
            }
        )
    )
    firstname = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control form-control-user",
                "placeholder": "Firstname"
            }
        )
    )
    lastname = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control form-control-user",
                "placeholder": "Lastname"
            }
        )
    )
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control form-control-user",
                "placeholder": "Password"
            }
        )
    )
    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control form-control-user",
                "placeholder": "Confirm Password"
            }
        )
    )
    email = forms.CharField(
        widget = forms.EmailInput(
            attrs={
                "class": "form-control form-control-user",
                "placeholder": "Enter E-mail"
            }
        )
    )

    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'username', 'email', 'password1', 'password2', 'is_admin', 'is_staff')
