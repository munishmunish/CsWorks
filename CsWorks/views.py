from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from myapp.forms import AdminForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')

def admin_login(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            return redirect('admindash.html')
    else:
        form = AdminForm()
    return render(request, 'admin_login.html', {'form': form})

def worker_login(request):
    return render(request, 'worker_login.html')

def client_login(request):
    return render(request, 'client_login.html')

def register(request):
    return render(request, 'register.html')