from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from myapp.forms import CreatUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')

# def admin_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('admindash'))
#         else:
#             messages.error(request, 'Invalid login details.')
#             return render(request, 'admin_login.html')
#     else:
#         return render(request, 'admin_login.html')

# def worker_login(request):
#     return render(request, 'worker_login.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admindash')
        else:
            messages.error(request, 'Incorrect Username or Password')
            return redirect('login')
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreatUserForm()
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created successfully for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)

@login_required(login_url='login')
def admin_dash(request):
    return render(request,'admindash.html')

@login_required(login_url='login')
def client_dash(request):
    return render(request,'clientdash.html')