from django.shortcuts import render

# Create your views here.
def admindash(request):
    return render(request,'admindash.html')
def Userfeedback(request):
    return render(request,'userfeedback.html')
def Userreports(request):
    return render(request, 'userreports.html')
def finalreport(request):
    return render(request, 'finalreport.html')
def Users(request):
    return render(request,'Users.html')
def addUser(request):
    return render(request,'addUser.html')
def viewUser(request):
    return render(request,'viewUser.html')
def viewjobs(request):
    return render(request, 'viewjobs.html')
def viewjobdetails(request):
    return render(request, 'viewjobdetails.html')

