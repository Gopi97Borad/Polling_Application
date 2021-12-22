from django.forms import ModelForm
from .models import User
from django import forms


class RegistrationForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput)
    user_name = forms.CharField(max_length=60, widget=forms.TextInput)

    class Meta:
        model = User
        fields = ['user_name', 'first_name', 'last_name', 'email', 'pwd']
