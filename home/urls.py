from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views

urlpatterns =[
   
    path('home/', views.home_view, name='index'),
    
]