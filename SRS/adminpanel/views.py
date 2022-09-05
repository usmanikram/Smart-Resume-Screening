from django.shortcuts import render
from base.models import User,Feedback,Report,Job
from .forms import addUserForm

# Create your views here.
def admindash(request):
    return render(request,'admindash.html')
def feedback(request):
    obj = Feedback.objects.all()
    context = {'obj': obj}
    
    return render(request,'Afeedback.html', context)
def reports(request):
    objR = Report.objects.all()
    context ={'objR' : objR}

    return render(request, 'Areports.html',context)
def finalreport(request):
    return render(request, 'finalreport.html')
def Users(request,):
    object = User.objects.all()
    return render(request,'Users.html',
    {'object' : object})
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
def viewUser(request, pk):
    user = User.objects.get(id=pk)
    context={'user':user}
    return render(request,'viewUser.html', context)

def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return render(request,'admindash.html')

def deleteJob(request, pk):
    job = Job.objects.get(id=pk)
    job.delete()
    return render(request,'admindash.html')


def viewjobs(request):
    obj=Job.objects.all()
    return render(request, 'viewjobs.html',
    { 'obj' :obj})
    

def viewjobdetails(request, pk):
    job= Job.objects.get(id=pk)
    context={'job':job}
    return render(request, 'Aviewjobdetails.html',context)    
