from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
#password = hjz+8fp.VnBQ5Qu

def home(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Ensure the field names match your HTML form
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/login')
