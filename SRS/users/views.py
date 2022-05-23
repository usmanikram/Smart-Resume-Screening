from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def editprofile(request):
    return render(request, 'editprofile.html')

def jobs(request):
    return render(request, 'jobs.html')


def addjob(request):
    return render(request, 'addjob.html')


def reports(request):
    return render(request, 'reports.html')
    
def insights(request):
    return render(request, 'insights.html')

def settings(request):
    return render(request, 'settings.html')