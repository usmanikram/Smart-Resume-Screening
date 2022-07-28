from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
    path('',views.admindash,name='admindash'),
    path('feedback',views.feedback,name='feedback'),
]