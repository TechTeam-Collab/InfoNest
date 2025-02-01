from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from .models import Account

# Create your views here.
def login_view(request):
  if request.method == 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')

      if not email or not password:
          return HttpResponse("<h1>Email and password are required.</h1>", status=400)

      try:
          user = Account.objects.get(email=email)
      except Account.DoesNotExist:
          return HttpResponse("<h1>Invalid email or password.</h1>", status=400)

      if check_password(password, user.password):
          name = user.last_name
          return HttpResponse(f"<h1>Login successful.</h1> { name }", status=200)
      else:
          return HttpResponse("<h1>Invalid email or password.</h1>", status=400)

  return render(request, 'account/login.html')

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if not first_name or not last_name or not email or not password or not confirm_password:
            return HttpResponse("<h1>All fields are required.</h1>", status=400)
        if password != confirm_password:
            return HttpResponse("<h1>Passwords do not match.</h1>", status=400)
        else:
            try:
                Account.objects.get(email=email)
                return HttpResponse("<h1>Email already exists.</h1>", status=400)
            except Account.DoesNotExist:
                pass
            user = Account(first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            return HttpResponse("<h1>Account created successfully</h1>")
        
    return render(request, 'account/signup.html')

def forgot_view(request):
  return render(request, 'account/forgot.html')

def verify_view(request):
  return render(request, 'account/verify.html')

def custom_404_view(request, exception):
    return render(request, 'account/404.html')