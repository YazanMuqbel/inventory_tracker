from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import User
from django.contrib import messages
import bcrypt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password


# Create your views here.

def home(request):
    return render(request, 'homepage.html')

def sign_up(request):
    return render(request, 'sign_up.html')

def sign_in(request):
    return render(request, 'sign_in.html')


# this function handles data from the form and creates a new user, and also handle the first name + shows SUCCESS page.
def create_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            
        return redirect('homepage')
    
    elif request.method == 'POST':
        params = dict()
        
        params['firstName'] = request.POST.get('firstName')
        params['lastName'] = request.POST.get('lastName')
        params['email'] = request.POST.get('email')
        pw_hash = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt()).decode()
        params['password'] = pw_hash
        #params['confirm_password'] = request.POST.get('confirm_password')

    user = User.objects.create(**params)
    
    return redirect('sign_in_page')

"""def dashboard(request):
    if request.method == 'POST':
    
        user = User.objects.filter(email=request.POST['email'])

    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('user_dashboard')
        
    return redirect('homepage')"""


def dashboard(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('control_panel')
    return redirect('homepage')


def control_panel(request):
    return render(request, 'dashboard.html')