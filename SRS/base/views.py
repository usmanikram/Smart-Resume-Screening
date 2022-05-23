from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def ok(request):
    return render(request, 'base/addUser.html')

def loginPage(request):
    return render(request, 'base/login_register.html')

