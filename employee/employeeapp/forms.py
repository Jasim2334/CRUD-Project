from cProfile import label
from attr import attr, fields
from django import forms
from .models import employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class signupForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget = forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        help_texts = {
            'username': None
        }

class Details(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['name', 'salary', 'designation', 'company']
        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control"}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),

        }
