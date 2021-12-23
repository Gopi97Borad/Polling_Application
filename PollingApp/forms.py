from django.forms import ModelForm
from .models import User
from django import forms


class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'first_name', 'last_name', 'email', 'pwd']
