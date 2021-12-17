from django.db.models import fields
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


# register form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Comment form
class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    body = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5,
        "placeholder": "Leave your comment here:"
    }), label='')
