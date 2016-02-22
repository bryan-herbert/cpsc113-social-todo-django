from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from splash.forms import RegisterForm, LoginForm

# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cleanData = form.cleaned_data
            if len(cleanData['name']) > 50:
                registrationForm = RegisterForm()
                loginForm = LoginForm()
                return render(request, 'splash/index.html', {'login': loginForm, 'registration': registrationForm, 'errors': 'Name is too long'})
            if len(cleanData['password']) > 50:
                registrationForm = RegisterForm()
                loginForm = LoginForm()
                return render(request, 'splash/index.html', {'login': loginForm, 'registration': registrationForm, 'errors': 'Password is too long'})
            if cleanData['password'] == cleanData['passwordConfirmation']:
                if User.objects.filter(username=cleanData['email']).exists():
                    registrationForm = RegisterForm()
                    loginForm = LoginForm()
                    return render(request, 'splash/index.html', {'login': loginForm, 'registration': registrationForm, 'errors': 'E-mail already exists'})
                else:
                    user = User.objects.create_user(cleanData['email'], '', cleanData['password'], first_name=cleanData['name'])
                    user = authenticate(username=cleanData['email'], password=cleanData['password'])
                    auth_login(request,user)
                    return HttpResponseRedirect('/')
            else:
                registrationForm = RegisterForm()
                loginForm = LoginForm()
                return render(request, 'splash/index.html', {'login': loginForm, 'registration': registrationForm, 'errors': 'Passwords do not match'})
        else:
            registrationForm = RegisterForm()
            loginForm = LoginForm()
            return render(request, 'splash/index.html', {'login': loginForm, 'registration': registrationForm, 'errors': 'Name too short'})
    return HttpResponseRedirect('/')
    
def login(request):
    #not sure if use post or get here, think get making no changes to database
    email=request.GET['email']
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
            return render(request, 'splash/index.html', {'login': loginForm, 'registration': registrationForm, 'errors': 'Invalid password'})
    else:
        registrationForm = RegisterForm()
        loginForm = LoginForm()
        return render(request, 'splash/index.html', {'login': loginForm, 'registration': registrationForm, 'errors': 'Invalid e-mail'})

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')