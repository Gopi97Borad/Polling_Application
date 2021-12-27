from django.forms import ModelForm
from .models import User, TaskList
from django import forms


class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'first_name', 'last_name', 'email', 'pwd']


class TaskForm(ModelForm):
    class Meta:
        model = TaskList
        fields = ['task_name']
        exclude = ['user', 'task_category', 'task_description']
        widgets = [{
            'user': forms.IntegerField(required=False),
            'task_category': forms.IntegerField(required=False),
            'task_description': forms.CharField(required=False)
        }]

        def __init__(self):
            self.field['task_name'].initial


class EditTaskForm(ModelForm):
    class Meta:
        model = TaskList
        fields = ['task_name']

