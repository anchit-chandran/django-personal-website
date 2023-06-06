from django.forms import ModelForm, TextInput, PasswordInput
from django import forms
from django.contrib.auth.models import User

from app_website.models import BlogPost


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

        widgets = {
            "username": TextInput(attrs={"class": "form-control"}),
            "password": PasswordInput(attrs={"class": "form-control"}),
        }

class CreatePostForm(ModelForm):
    
    class Meta:
        model = BlogPost
        fields = "__all__"
        
        widgets = {
            "posted_at": forms.DateInput(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "header_img": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "featured": forms.CheckboxInput(attrs={"class": "form-control"}),
        }