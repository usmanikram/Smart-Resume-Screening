from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
    path('',views.admindash,name='admindash'),
    path('Areports',views.reports,name='reports'),
]