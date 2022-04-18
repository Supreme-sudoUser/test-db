from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User, auth



def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()

    context = {
        'form': form,
        'msg': msg,
    }
    return render(request, 'user/register.html', context)

def login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            msg = 'invalid credetial'
    else:
        msg = 'error with form'
    
    context = {
        'form': form,
        'msg': msg,
    }
    # return render(request, 'userpage.html')
    return render(request, 'user/login.html', context)

def logout(request):
    logout(request)
    return redirect('')

def forgotpassword(request):
    return render(request, 'user/forgot-password.html')

