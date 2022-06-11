from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')
  
def signup(request):
    return render(request, 'base/signup.html')
  
def ok(request):
    return render(request, 'base/addUser.html')

def login(request):
    return render(request, 'base/login.html')
