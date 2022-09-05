from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
    path('',views.admindash,name='admindash'),
    path('feedback',views.feedback,name='feedback'),
    path('reports',views.reports,name='reports'),
    path('finalreport',views.finalreport,name='finalreport'),
    path('Users',views.Users,name='Users'),
    path('addUser',views.addUser,name='addUser'),
    path('viewUser/<str:pk>',views.viewUser,name='viewUser'),
    path('deleteUser/<str:pk>',views.deleteUser,name='deleteUser'),
    path('deleteJob/<str:pk>',views.deleteJob,name='deleteJob'),
    path('viewjobs',views.viewjobs,name='viewjobs'),
    path('viewjobdetails/<str:pk>',views.viewjobdetails,name='viewjobdetails'),
  ]

