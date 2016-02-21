from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("What's up Doc? You're at the Tasks Index")
    
def createTask (request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            cleanData = form.cleaned_data
            task = Task(owner=request.user, title=cleanData['title'], description=cleanData['description'])
            task.save()
            task.collaborators.add(cleanData['collaborator1'])
            task.collaborators.add(cleanData['collaborator2'])
            task.collaborators.add(cleanData['collaborator3'])
            task.save()
    
    return HttpResponseRedirect('/')

def deleteTask (request):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        task.delete()

    return HttpResponseRedirect('/')
    
def toggleTask(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        if task.isComplete == True:
            task.isComplete = False
        else:
            task.isComplete = True

        task.save()

    return HttpResponseRedirect('/')