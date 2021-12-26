# from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView

from . import user_login
from .forms import RegistrationForm, TaskForm, EditTaskForm
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
                request.session['user'] = username.id
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
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'polls/user_registration.html', context={'form': form})


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
        else:
            print('called!!!!')
            form = TaskForm()
            return render(request, 'polls/home.html', context={'form': form, "tasks": tasks})
        return render(request, 'polls/home.html', context={'form': form, "tasks": tasks})
    return redirect('/')


def delete(request, task_id):
    print('called')
    if request.session.get('user'):
        TaskList.objects.get(id=task_id).delete()
        # TaskList.refresh_from_db(self)
        tasks = TaskList.objects.filter(user_id=request.session.get('user'))
        print(tasks)
        return redirect('/home')
    return redirect('/')


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


def update(request, task_id, category_id):
    if request.session.get('user'):
        task = TaskList
        task = TaskList.objects.get(id=task_id)
        if task:
            task.task_category = category_id
            task.save()
        return HttpResponseRedirect('/home')
    return redirect('/')


def logout_d(request):
    del request.session['user']
    return redirect('/')
