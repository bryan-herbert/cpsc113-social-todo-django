from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cleanData = form.cleaned_data
            if cleanData['password'] == data ['password_confirmation']:
                user = User.objects.create_user(data['email'], '', data['password'], first_name=data['fl_name'])
                user = authenticate(username=cleanData['email'], password=cleanData['password'])
                auth_login(request,user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('Passwords do not match')
        else:
            registrationForm = RegisterForm()
            return render(request, 'splash/index.html', {'register': registrationForm})
    return HttpResponseRedirect('/')

def login(request):
    #not sure if use post or get here, think get making no changes to database
    email=request.GET['email]
    password=request.GET['password']
    if User.objects.filer(username=email).exists():
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('Error signing in')
            
        else:
            registrationForm = RegisterForm()
            loginForm = LoginForm()
            return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Invalid password'})
    else:
        registrationForm = RegisterForm()
        loginForm = LoginForm()
        return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm, 'errors': 'Invalid e-mail'})




def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')