from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from .models import Account

# Create your views here.
def login_view(request):
  if request.method == 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')

      if not email or not password:
          return HttpResponse("Email and password are required.", status=400)

      try:
          account = Account.objects.get(email=email)
      except Account.DoesNotExist:
          return HttpResponse("Invalid email or password.", status=400)

      if check_password(password, account.password):
          return HttpResponse("Login successful.", status=200)
      else:
          return HttpResponse("Invalid email or password.", status=400)

  return render(request, 'account/login.html')

def signup_view(request):
  return render(request, 'account/signup.html')

def forgot_view(request):
  return render(request, 'account/forgot.html')

def verify_view(request):
  return render(request, 'account/verify.html')