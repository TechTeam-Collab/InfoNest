from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404


handler404 =  "account.views.custom_404_view"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('',include('account.urls')),
]
