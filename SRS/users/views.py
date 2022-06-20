from django.shortcuts import render

# Create your views here.
def dashboard(request):
    context = {"segment" : "dashboard"}
    return render(request, 'dashboard.html', context)

def editprofile(request):
    context = {"segment" : "editprofile"}
    return render(request, 'editprofile.html', context)

def jobs(request):
    context = {"segment" : "jobs"}
    return render(request, 'jobs.html', context)

def createjob(request):
    context={"segment": "createjob"}
    return render(request, 'createjob.html',context)

def viewjobs(request):
    context={"segment":"viewjobs"}
    return render(request, 'viewjobs.html')

def reports(request):
    context = {"segment" : "reports"}
    return render(request, 'reports.html', context)

def feedback(request):
    context = {"segment" : "feedback"}
    return render(request, 'feedback.html', context)
    
def addfeedback(request):
    context = {"segment" : "addfeedback"}
    return render(request, 'addfeedback.html', context)

def insights(request):
    context = {"segment" : "insights"}
    return render(request, 'insights.html', context)

def settings(request):
    context = {"segment" : "settings"}
    return render(request, 'settings.html', context)
