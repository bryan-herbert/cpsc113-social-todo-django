from django.shortcuts import render
from django.http import HttpResponseRedirect
from splash.forms import newTaskForm
import pdb
from tasks.models import Task
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return HttpResponse("What's up Doc? You're at the Tasks Index")
    
def create(request):
    if request.method == 'POST':
        form = newTaskForm(request.POST)
        print "GOT HERE1"
        if form.is_valid():
            print "GOT HERE2"
            cleanData = form.cleaned_data
            task = Task(owner=request.user, title=request.POST.get('title'), description=request.POST.get('description'))
            task.save()
            if User.objects.filter(username=cleanData['collaborator1']).exists():
                task.collaborators.add(User.objects.get(username=cleanData['collaborator1']))
            if User.objects.filter(username=cleanData['collaborator2']).exists():
                task.collaborators.add(User.objects.get(username=cleanData['collaborator2']))
            if User.objects.filter(username=cleanData['collaborator3']).exists():
                task.collaborators.add(User.objects.get(username=cleanData['collaborator3'])) 
            task.save()
            print "GOT HERE3"
    return HttpResponseRedirect('/')

def delete (request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        task.delete()
    return HttpResponseRedirect('/')
    
def toggle(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        if task.isComplete == True:
            task.isComplete = False
        else:
            task.isComplete = True
        task.save()
    return HttpResponseRedirect('/')