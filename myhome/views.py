from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    return render(request, 'pages/myhome.html')


def mycontact(request):
    return render(request, 'pages/mycontact.html')


def error(request, exception):
    return render(request, 'pages/error.html', {'message': exception})


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})


def developing(request):
    return render(request, 'pages/developing.html')