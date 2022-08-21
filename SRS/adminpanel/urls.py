from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
    path('',views.admindash,name='admindash'),
    path('Userfeedback',views.Userfeedback,name='Userfeedback'),
    path('Userreports',views.Userreports,name='Userreports'),
    path('finalreport',views.finalreport,name='finalreport'),
    path('Users',views.Users,name='Users'),
    path('addUser',views.addUser,name='addUser'),
    path('viewUser',views.viewUser,name='viewUser'),
    path('viewjobs',views.viewjobs,name='viewjobs'),
    path('viewjobdetails',views.viewjobdetails,name='viewjobdetails'),
  ]

