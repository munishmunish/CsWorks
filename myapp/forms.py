from django import forms
from myapp.models import Admin, Worker, Client

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.contrib.auth.forms import UserCreationForm

class AdminForm(forms.Form):
    class Meta:
        model = Admin
        fields = ['username', 'password']
        labels = {'username': u'Username', 'password': u'Password'}