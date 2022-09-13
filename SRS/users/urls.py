from django.urls import path
from . import views
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
path('',views.dashboard,name='dashboard'),
path('Logout', views.Logout, name="Logout"),
path('editprofile/<str:pk>',views.editprofile,name='editprofile'),
path('editprofile/update/<str:pk>',views.update,name='update'),
path('jobs/<str:pk>',views.jobs,name='jobs'),
path('viewjobdetails/<str:pk>',views.viewjobdetails,name='viewjobdetailsuser'),
path('editjob/<str:pk>',views.editjob,name='editjob'),
path('updatejob/<str:pk>',views.updatejob,name='updatejob'),
path('deletejob/<str:pk>',views.deletejob,name='deletejob'),
path('feedback/<str:pk>',views.feedback,name='feedback'),
path('pendingfeedback/<str:pk>',views.pendingfeedback,name='pendingfeedback'),
path('addfeedback/<str:pk>',views.addfeedback,name='addfeedback'),
path('viewfeedback/<str:pk>',views.viewfeedback,name='viewfeedback'),
path('deletefeedback/<str:pk>',views.deletefeedback,name='deletefeedback'),
path('reports/<str:pk>',views.reports,name='reports'),
path('insights',views.insights,name='insights'),
path('settings',views.settings,name='settings'),
path('createjob/<str:pk>',views.createjob, name='createjob'),
path('reporttemplate/<str:pk>',views.reporttemplate,name='reporttemplate'),
path('finalreport',views.finalreport,name='finalreport'),
path('shortlist/<str:pk>',views.shortlist,name='shortlist'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

