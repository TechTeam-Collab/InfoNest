from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
  path('', views.login_view, name='login'),
  path('signup/', views.signup_view, name="signup"),
  path('forgot/', views.forgot_view, name="forgot"),
  path('verify/', views.verify_view, name="verify"),
]
