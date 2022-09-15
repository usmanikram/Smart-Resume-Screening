from django.shortcuts import render, redirect
from .forms import UserForm,LoginForm,CreateJobForm,CreateJobFormForResume,SignupForm
from .models import Resume,Candidate
# from .parser import get_resume_data
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


#from pyresparser import ResumeParser
# Create your views here.

def home(request):
    return render(request, 'base/home.html')
  
def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():

            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()

            messages.success(request, 'success')
            return redirect('loginuser')
    context = {"segment" : "Sign Up",'form':form}
    return render(request, 'base/signup.html',context)
  
def ok(request):
    return render(request, 'base/addUser.html')

def loginuser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect ('adminpanel/', pk=user.id)
            
            if user.is_approved:
                login(request, user)
                return redirect('users/', pk=user.id)
            else:
                messages.info(request, 'fail')

        else:
            messages.info(request, 'fail2')
    
    context = {"segment" : "Sign In"}
    return render(request, 'base/login.html',context)




def test(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()

            messages.success(request, 'Account successfully created.')
            return redirect('login')
    context = {'form':form}
    return render(request,'base/test.html',context)



# def cjob(request):

#     if request.method == 'POST':
#         jobform = CreateJobForm(request.POST , request.FILES)
#         resumeform = CreateJobFormForResume(request.POST , request.FILES)
#         if jobform.is_valid() and resumeform.is_valid():
#             j = jobform.save()
#             r = resumeform.save(commit = False)
#             r.job_id  = j
#             r.save()
#     else:
#         jobform = CreateJobForm()
#         resumeform = CreateJobFormForResume()
#     context = {'jobform':jobform, 'resumeform':resumeform}
#     return render(request,'base/cjob.html',context)

def cjob(request):

    if request.method == 'POST':
        jobform = CreateJobForm(request.POST , request.FILES)
        resumeform = CreateJobFormForResume(request.POST , request.FILES)
        files = request.FILES.getlist('file_path')
        if jobform.is_valid():
            j = jobform.save()
            for f in files:   
                r = Resume(job_id=j, file_path=f)
                r.save()
                #data = ResumeParser(r.file_path.path).get_extracted_data()
                #c = Candidate(job_id=r.job_id,name=data['name'],contact=data['mobile_number'],email=data['email'],resume=r.file_path)
                c.save()
    else:
        jobform = CreateJobForm()
        resumeform = CreateJobFormForResume()
    context = {'jobform':jobform ,'resumeform':resumeform}
    return render(request,'base/cjob.html',context)



def rjob(request):

    if request.method == 'POST':
        resumeform = CreateJobFormForResume(request.POST , request.FILES)
        if resumeform.is_valid():
            resumeform.save()
            print('Saved')
    else:
        resumeform = CreateJobFormForResume()
    context = {'resumeform':resumeform}
    return render(request,'base/rjob.html',context)