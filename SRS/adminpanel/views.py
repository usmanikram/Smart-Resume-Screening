from django.shortcuts import render

# Create your views here.
def admindash(request):
    return render(request,'admin/admindash.html')


def feedback(request):
    return render(request,'admin/feedback.html')