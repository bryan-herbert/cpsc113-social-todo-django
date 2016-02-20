from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm
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
            
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')