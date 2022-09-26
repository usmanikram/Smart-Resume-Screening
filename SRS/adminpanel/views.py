from django.shortcuts import render, redirect
from base.models import User,Feedback,Report,Job
from .forms import addUserForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='loginuser')
def admindash(request):
    return render(request,'admindash.html')

@login_required(login_url='loginuser')
def feedback(request):
    obj = Feedback.objects.all()
    context = {'obj': obj}
    
    return render(request,'Afeedback.html', context)

@login_required(login_url='loginuser')
def reports(request):
    objR = Report.objects.all()
    context ={'objR' : objR}

    return render(request, 'Areports.html',context)

@login_required(login_url='loginuser')
def finalreport(request):
    return render(request, 'finalreport.html')

@login_required(login_url='loginuser')
def Users(request,):
    object = User.objects.filter(is_staff = 'False', is_approved = 'True')
    return render(request,'Users.html',
    {'object' : object})

@login_required(login_url='loginuser')
def approveUser(request):
    object = User.objects.filter(is_approved = 'False')
    return render(request,'approveUser.html',
    {'object' : object})

@login_required(login_url='loginuser')
def approveUserFunc(request, pk):
    user = User.objects.get(id = pk)
    user.is_approved = 'True'
    user.save()
    return redirect ('Users')

@login_required(login_url='loginuser')
def addUser(request):
    form = addUserForm()
    if request.method== 'POST':
        form = addUserForm(request.POST)
        if form.is_valid():

            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()

            # messages.success(request, 'Account successfully created.')
            # return redirect('')
    context = {"segment" : "AddUser",'form':form}
    return render(request, 'addUser.html',context)

@login_required(login_url='loginuser')
def viewUser(request, pk):
    user = User.objects.get(id=pk)
    context={'user':user}
    return render(request,'viewUser.html', context)

@login_required(login_url='loginuser')
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return render(request,'admindash.html')

@login_required(login_url='loginuser')
def deleteJob(request, pk):
    job = Job.objects.get(id=pk)
    job.delete()
    return render(request,'admindash.html')

@login_required(login_url='loginuser')
def viewjobs(request):
    obj=Job.objects.all()
    return render(request, 'viewjobs.html',
    { 'obj' :obj})
    
@login_required(login_url='loginuser')
def viewjobdetails(request, pk):
    job= Job.objects.get(id=pk)
    context={'job':job}
    return render(request, 'Aviewjobdetails.html',context)    

