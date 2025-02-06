from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages



@login_required(login_url='/login')
def admin_view(request, name):
                """
                Admin view for superusers.
                """
                if not request.user.is_superuser:
                    return HttpResponse("<h1>Unauthorized Access</h1>", status=403)
                return render(request, 'account/admin_page.html', {'name': name})

class CustomLoginView(LoginView):
                """
                Custom login view for handling both admin and regular user logins.
                """
                template_name = 'account/login.html'

                def get(self, request, *args, **kwargs):
                    return render(request, self.template_name)

                def post(self, request, *args, **kwargs):
                    email = request.POST.get('email')
                    password = request.POST.get('password')
                    remember_me = request.POST.get('remember_me')

                    if not email or not password:
                        messages.error(request, 'Please enter your email and password.')
                        return redirect('/')
                    try:
                        user = User.objects.get(email=email)
                    except User.DoesNotExist:
                        messages.error(request, 'User does not exist.')
                        return redirect('login')

                    user = authenticate(request, username=user.username, password=password)
                    if user is not None:
                        login(request, user)
                        if remember_me:
                            request.session.set_expiry(60 * 60 * 24 * 7)
                        else:
                            request.session.set_expiry(0)
                        if user.is_superuser:
                            name = user.username
                            return redirect(f'/admin_page/{name}/')
                        else:
                            name = user.username
                            return render(request, 'profile/user_page.html')
                    else:
                        messages.error(request, 'Invalid login details.')
                        return redirect('login')


def signup_view(request):
                """
                Handles user signup.
                """
                if request.method == 'POST':
                    first_name = request.POST.get('first_name')
                    last_name = request.POST.get('last_name')
                    email = request.POST.get('email')
                    password = request.POST.get('password')
                    confirm_password = request.POST.get('confirm_password')

                    if not first_name or not last_name or not email or not password or not confirm_password:
                        return HttpResponse("<h1>All fields are required.</h1>", status=400)
                    if password != confirm_password:
                        messages.error(request, 'Passwords do not match.')
                        return redirect('signup')
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'Email already exists.')
                        return redirect('signup')

                    user = User.objects.create_user(
                        username=email,  # Use email as the username
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=password
                    )
                    user.save()
                    return redirect('login')
                return render(request, 'account/signup.html')


def forgot_view(request):
                """
                Forgot password view.
                """
                return render(request, 'account/forgot.html')


def verify_view(request):
                """
                Email verification view.
                """
                return render(request, 'account/verify.html')


def custom_404_view(request, exception):
                """
                Custom 404 error page.
                """
                return render(request, 'account/404.html')


def logout_view(request):
                """
                Handles user logout.
                """
                logout(request)
                return redirect('/')


name="admin"
@login_required(login_url='/login')
def user_list_view(request,name):
        users = User.objects.all()
        if not request.user.is_superuser:
            return HttpResponse("<h1>Unauthorized Access</h1>", status=403)
        return render(request, 'account/user_list.html', {'users': users})



@staff_member_required(login_url='/')
def admin_edit_user_view(request,user_id):
        user = get_object_or_404(User, id=user_id)
        if request.method == 'POST':
            user.username = request.POST.get('username')
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.role = request.POST.get('role')
            user.password = request.POST.get('password')
            user.save()
            messages.success(request, f"User {user.username}'s profile has been updated successfully!")
            return redirect('user_list', name="admin")  

        return render(request, 'account/admin_edit_user.html', {'user': user})

# admin delete user
@staff_member_required(login_url='/')
def admin_delete_user_view(request,user_id):
        user = get_object_or_404(User, id=user_id)
        if request.method == 'POST':
            user.delete()
            messages.success(request, f"User {user.username} has been deleted successfully!")
            return redirect('user_list', name="admin")
        return render(request, 'account/admin_delete_user.html', {'username': user.username})


            