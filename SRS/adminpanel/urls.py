from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
    path('',views.admindash,name='admindash'),
    path('Users',views.Users,name='Users'),
    path('addUser',views.addUser,name='addUser'),
    path('viewUser',views.viewUser,name='viewUser'),
  ]