from django.urls import path
from .import views
from django.shortcuts import render

urlpatterns = [
    path('',views.home, name="home"),
    path('addUser',views.ok , name="addUser"),
    path('login',views.login , name="login"),
    path('signup',views.signup,name='signup'),
    path('signupuser',views.signup,name='signupuser'),
]

