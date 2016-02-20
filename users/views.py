from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")
    
def say_whatsup(request):
    return HttpResponse("Hello, WHAT IS UP?")