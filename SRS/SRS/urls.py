
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls'))
=======
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)
>>>>>>> 0175ca392b5b6ac57fffd9bd37a8ac1f12ea39c2
]
