from django.shortcuts import render
from django.http import HttpResponseRedirect
# Changed it to HttpResponseRedirect

# Create your views here.

#def index(request):
#   return render(request, 'index.html')

from .forms import RegisterForm

def get_registration(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # IMPORTANT- changed it from a different url back to the homepage
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()
        
    return render(request, 'index.html', {'form': form})
    
    
