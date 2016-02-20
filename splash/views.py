from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.db.models import Q
# Changed it to HttpResponseRedirect

# Create your views here.

#def index(request):
#   return render(request, 'index.html')

from .forms import RegisterForm

def index(request):
    registrationForm = RegisterForm();
    loginForm = LoginForm()
    return render(request, 'splash/index.html', {'login': loginForm, 'register': registrationForm})
    
    
