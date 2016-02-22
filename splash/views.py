from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import newTaskForm
from tasks.models import Task
from .forms import RegisterForm
from .forms import LoginForm
from django.contrib.auth.models import User
from django.db.models import Q
# Changed it to HttpResponseRedirect

# Create your views here.

#def index(request):
#   return render(request, 'index.html')

from .forms import RegisterForm

def index(request):
    if request.user.is_authenticated():
        tasks = Task.objects.filter(Q(owner=request.user) | Q(collaborators=request.user))
        return render(request, 'index.html', {'user': request.user, 'new_task': newTaskForm, 'tasks': tasks})
    else:
        registrationForm = RegisterForm()
        loginForm = LoginForm()
        return render(request, 'index.html', {'login': loginForm, 'registration': registrationForm})