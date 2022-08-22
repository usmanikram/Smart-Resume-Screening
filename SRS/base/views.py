from django.shortcuts import render
from django.views.generic import CreateView
from .models import Users
from .forms import SignupUserForm
# Create your views here.

def home(request):
    return render(request, 'base/home.html')
  
def signup(request):
    form = SignupUserForm()
    if request.method == 'POST':
        form = SignupUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'base/signupuser.html',context)
    # context = {"segment" : "Sign Up"}
    # return render(request, 'base/signup.html',context)
  
def ok(request):
    return render(request, 'base/addUser.html')

def login(request):
    context = {"segment" : "Sign In"}
    return render(request, 'base/login.html',context)

# class AddUsersCreateView(CreateView):
#     model=Users
#     fields=('firstname','lastname','contact','designation','company_name','company_contact','company_address','email','password','creation_date','is_approved')