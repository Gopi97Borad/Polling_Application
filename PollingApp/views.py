# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import user_login


def login(request):
    context = {}
    form = user_login.LoginForm()
    message = ''
    if request.method == 'POST':
        form = user_login.LoginForm(request.POST)
        if form.is_valid():
            pass
            user = form.cleaned_data['username']
            if user != '':
                message = 'you have been Loged In'
                return HttpResponseRedirect('home/')
            else:
                message = 'Log in Failed'
    return render(request, 'polls/user_login.html', context={'form': form, 'message': message})


def home(request):
    context = {}
    return render(request, 'polls/home.html', context)


def create(request):
    context = {}
    return render(request, 'polls/create.html', context)


def results(request):
    context = {}
    return render(request, 'polls/results.html', context)


def vote(request):
    context = {}
    return render(request, 'polls/vote.html', context)
