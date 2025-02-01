from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import handler404
from . import views

handler404 =  "account.views.custom_404_view"

urlpatterns = [
  path('', views.login_view, name='login'),
  path('signup/', views.signup_view, name="signup"),
  path('forgot/', views.forgot_view, name="forgot"),
  path('verify/', views.verify_view, name="verify"),
]
