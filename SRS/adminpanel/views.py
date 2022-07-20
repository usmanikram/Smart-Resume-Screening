from django.shortcuts import render

# Create your views here.
def admindash(request):
    return render(request,'admindash.html')
def reports(request):
    return render(request, 'reports.html')
def finalreport(request):
    return render(request, 'finalreport.html')