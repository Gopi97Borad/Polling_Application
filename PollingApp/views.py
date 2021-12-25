# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import user_login
from .forms import RegistrationForm, TaskForm
from .models import *
from django.contrib import messages


def login(request):
    context = {}
    form = user_login.LoginForm()
    message = ''
    if request.method == 'POST':
        form = user_login.LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            username = User.objects.get(user_name=form.cleaned_data['username'])

            if username.user_name == user_name and username.pwd == pwd:
                response = HttpResponseRedirect('home/')
                response.set_cookie('user', username.id, max_age=None, expires=None)
                return response
            else:
                messages.info(request, 'Your Username or Password is Invalid')
                return render(request, 'polls/user_login.html', context={'form': form, 'message': message})
    return render(request, 'polls/user_login.html', context={'form': form})


def create(request):
    context = {}
    return render(request, 'polls/create.html', context)


def results(request):
    context = {}
    return render(request, 'polls/results.html', context)


def vote(request):
    context = {}
    return render(request, 'polls/vote.html', context)


def registration(request):
    form = RegistrationForm(request.POST)
    print(form)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'polls/user_registration.html', context={'form': form})


def home(request):
    form = TaskForm()
    task = TaskList()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = User.objects.get(user_name=request.COOKIES.get('user'))
            task.task_name = form.cleaned_data['task_name']
            task.user = username
            task.task_category = 1
            task.save()
    return render(request, 'polls/home.html', context={'form': form})
