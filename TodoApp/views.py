# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from . import user_login
from .forms import RegistrationForm, TaskForm
from .models import *
from django.contrib import messages


# used for successful login based on username and password of already exist user
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
                request.session['user'] = username.id
                return response
            else:
                messages.info(request, 'Your Username or Password is Invalid')
                return render(request, 'layouts/user_login.html', context={'form': form, 'message': message})
    return render(request, 'layouts/user_login.html', context={'form': form})


# used to save the registration data of new user
def registration(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'layouts/user_registration.html', context={'form': form})


# function to add new task in model
def home(request, task_id=''):
    print(request)
    tasks_list = TaskList
    if request.session.get('user'):
        form = TaskForm()
        task = TaskList()
        tasks = TaskList.objects.filter(user_id=request.session.get('user'))
        if request.method == 'POST':
            print('register')
            form = TaskForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                username = User.objects.get(id=request.session.get('user'))
                task.task_name = form.cleaned_data['task_name']
                task.user = username
                task.task_category = 1
                task.save()
                form = TaskForm()
                return HttpResponseRedirect("/home")
        else:
            form = TaskForm()
            return render(request, 'layouts/home.html', context={'form': form, "tasks": tasks})
        return render(request, 'layouts/home.html', context={'form': form, "tasks": tasks})
    return redirect('/')


# function to delete particular task
def delete(request, task_id):
    print('called')
    if request.session.get('user'):
        TaskList.objects.get(id=task_id).delete()
        tasks = TaskList.objects.filter(user_id=request.session.get('user'))
        print(tasks)
        return redirect('/home')
    return redirect('/')


# function to edit particular task's task name
def editTask(request, task_id):
    form = TaskForm()
    if request.method == 'POST':
        tasks = TaskList.objects.filter(user_id=request.session.get('user'))
        form = TaskForm(request.POST)
        if form.is_valid():
            task = TaskList.objects.get(id=task_id)
            task.task_name = form.cleaned_data['task_name']
            task.id = task_id
            task.save()
        return redirect('/home')
    return redirect('/')


# function to update user information
def updateUserData(request):
    form = RegistrationForm()
    user = User.objects.get(id=request.session.get('user'))
    if request.session.get('user'):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            print(request.POST)
            if form.is_valid():
                print('called')
                user.user_name = form.cleaned_data['user_name']
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.email = form.cleaned_data['email']
                user.pwd = form.cleaned_data['pwd']
                user.save()
                form = RegistrationForm()
                return HttpResponseRedirect("/home/account")
        form = RegistrationForm()
        return render(request, 'layouts/myaccount.html', context={'form': form, 'user': user})
    return redirect('/')

# function to update task category Ex. From to do -> done
def update(request, task_id, category_id):
    if request.session.get('user'):
        task = TaskList
        task = TaskList.objects.get(id=task_id)
        if task:
            task.task_category = category_id
            task.save()
        return HttpResponseRedirect('/home')
    return redirect('/')


# function to handle user logout
def logout_d(request):
    del request.session['user']
    return redirect('/')
