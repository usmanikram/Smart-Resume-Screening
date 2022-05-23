from django.urls import path
from .import views
from django.shortcuts import render

urlpatterns = [
    path('',views.home, name="home"),
    path('addUser/',views.ok , name="addUser"),
    path('login/',views.loginPage , name="login"),
]