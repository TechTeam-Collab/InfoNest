from django.shortcuts import render

# Create your views here.
def login_view(request):
  return render(request, 'account/login.html')

def signup_view(request):
  return render(request, 'account/signup.html')

def forgot_view(request):
  return render(request, 'account/forgot.html')

def verify_view(request):
  return render(request, 'account/verify.html')