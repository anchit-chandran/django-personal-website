from django.forms import ModelForm, TextInput, PasswordInput
from django.contrib.auth.models import User


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

        widgets = {
            "username": TextInput(attrs={"class": "form-control"}),
            "password": PasswordInput(attrs={"class": "form-control"}),
        }
