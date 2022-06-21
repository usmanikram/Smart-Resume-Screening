from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')
  
def signup(request):
    context = {"segment" : "Sign Up"}
    return render(request, 'base/signup.html',context)
  
def ok(request):
    return render(request, 'base/addUser.html')

def login(request):
    context = {"segment" : "Sign In"}
    return render(request, 'base/login.html',context)
