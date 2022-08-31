from django.urls import path
from .import views
from django.shortcuts import render

urlpatterns = [
    path('',views.home, name="home"),
    path('addUser',views.ok , name="addUser"),
    path('login',views.loginuser , name="loginuser"),
    path('signup',views.signup,name='signup'),
    path('test',views.test,name='test'),
    path('cjob',views.cjob,name='cjob'),
    path('rjob',views.rjob,name='rjob'),
]

