from django.shortcuts import render
from django.http import HttpResponseRedirect
# Changed it to HttpResponseRedirect

# Create your views here.

#def index(request):
#   return render(request, 'index.html')

from .forms import RegisterForm

def index(request):
    registrationForm = RegisterForm();
    return render(request, 'index.html', {'register': registrationForm})
    
    
