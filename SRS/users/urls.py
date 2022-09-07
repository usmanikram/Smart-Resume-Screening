from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
path('',views.dashboard,name='dashboard'),
path('Logout', views.Logout, name="Logout"),
path('editprofile/<str:pk>',views.editprofile,name='editprofile'),
path('editprofile/update/<str:pk>',views.update,name='update'),
path('jobs/<str:pk>',views.jobs,name='jobs'),
path('viewjobdetails/<str:pk>',views.viewjobdetails,name='viewjobdetails'),
path('editjob/<str:pk>',views.editjob,name='editjob'),
path('updatejob/<str:pk>',views.updatejob,name='updatejob'),
path('deletejob/<str:pk>',views.deletejob,name='deletejob'),
path('feedback',views.feedback,name='feedback'),
path('addfeedback',views.addfeedback,name='addfeedback'),
path('reports',views.reports,name='reports'),
path('insights',views.insights,name='insights'),
path('settings',views.settings,name='settings'),
path('createjob/<str:pk>',views.createjob, name='createjob'),
path('viewjobs',views.viewjobs,name='viewjobs'),
path('finalreport',views.finalreport,name='finalreport'),
path('shortlist/<str:pk>',views.shortlist,name='shortlist'),




]

