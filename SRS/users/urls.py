from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
path('',views.dashboard,name='dashboard'),
path('editprofile',views.editprofile,name='editprofile'),
path('jobs',views.jobs,name='jobs'),
path('feedback',views.feedback,name='feedback'),
path('addfeedback',views.addfeedback,name='addfeedback'),
path('reports',views.reports,name='reports'),
path('insights',views.insights,name='insights'),
path('settings',views.settings,name='settings'),
path('createjob',views.createjob, name='createjob'),
path('viewjobs',views.viewjobs,name='viewjobs'),
path('finalreport',views.finalreport,name='finalreport'),

path('viewjobdetails',views.viewjobdetails,name='viewjobdetails'),
path('editjob',views.editjob,name='editjob'),
]

