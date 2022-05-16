from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
path('',views.dashboard,name='dashboard'),
path('editprofile',views.editprofile,name='editprofile'),
path('jobs',views.jobs,name='jobs'),
path('reports',views.reports,name='reports'),
]