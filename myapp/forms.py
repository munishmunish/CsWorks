from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from myapp.models import Project, Skills
from datetime import date
from django.core.validators import MaxValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class CreatUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'first_name','last_name','password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username *','class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email *','class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name *','class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name *','class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(CreatUserForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password *'})
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password *'})
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class CreateProjectForm(forms.ModelForm):
    end_date = forms.DateField(
        widget=forms.DateInput(),
        # validators=[MaxValueValidator(limit_value=date.today()),
    )

    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['title', 'description', 'start_date', 'end_date', 'total_work_hours', 'point_per_hour']

    def __init__(self, *args, **kwargs):
        super(CreateProjectForm, self).__init__(*args, **kwargs)

        self.fields['start_date'].required = True
        # self.fields['end_date'].required = True


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'