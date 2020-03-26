from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from myapp.models import Admin, Worker, Client
from django.contrib.auth.forms import UserCreationForm

class CreatUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'first_name','last_name','password1', 'password2']

