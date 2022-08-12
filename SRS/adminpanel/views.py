from django.shortcuts import render

# Create your views here.
def admindash(request):
    return render(request,'admindash.html')
def feedback(request):
    return render(request,'feedback.html')
def reports(request):
    return render(request, 'reports.html')
def finalreport(request):
    return render(request, 'finalreport.html')
def Users(request):
    return render(request,'Users.html')
def addUser(request):
    return render(request,'addUser.html')
def viewUser(request):
    return render(request,'viewUser.html')

