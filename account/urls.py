from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from django.conf import settings
from django.conf.urls import handler404
from . import views

handler404 =  "account.views.custom_404_view"

urlpatterns = [

  path('login/', views.CustomLoginView.as_view(template_name='account/login.html'), name='login'),
  path('signup/', views.signup_view, name="signup"),
  path('forgot/', views.forgot_view, name="forgot"),
  path('verify/', views.verify_view, name="verify"),
  path('admin_page/<str:name>/', views.admin_view, name="admin_page"),
  path('admin_page/<str:name>/user_list/', views.user_list_view, name="user_list"),
  path('admin_page/edit-user/<int:user_id>/', views.admin_edit_user_view, name='edit_user_admin'),
  path('admin_page/delete-user/<int:user_id>/', views.admin_delete_user_view, name='delete_user_admin'),
  path('logout/', views.logout_view, name="logout"),
]
