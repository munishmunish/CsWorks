from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login

from myapp.decorators import unauthenticated_user, allowed_users, admin_only
from myapp.forms import CreatUserForm, CreateProjectForm, SkillForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from myapp.models import Project, Skills

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')

@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            admin_user = Group.objects.get(name="admin").user_set.all()
            if user in admin_user:
                login(request, user)
                return redirect('admindash')
            client_user = Group.objects.get(name="client").user_set.all()
            if user in client_user:
                login(request, user)
                return redirect('clientdash')
            worker_user = Group.objects.get(name="worker").user_set.all()
            if user in worker_user:
                login(request, user)
                return redirect('workerdash')
        else:
            messages.error(request, 'Incorrect Username or Password')
            return redirect('login')
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def register(request):
    form = CreatUserForm()
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name="client")
            user.groups.add(group)

            messages.success(request, 'Account was created successfully for ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


@login_required(login_url='login')
def admin_dash(request):
    projects = Project.objects.filter(status=1)
    skills = Skills.objects.all()
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            skill = form.cleaned_data.get('skill')
            messages.success(request, "New Skill " + skill + " added to the database")
            return render(request, 'admindash.html', {'projects': projects, 'skills': skills, 'form': form})
    return render(request, 'admindash.html', {'projects': projects, 'skills': skills, 'form': form})

@login_required(login_url='login')
# @allowed_users(allowed_roles=['client'])
# @admin_only
def client_dash(request):
    projects = Project.objects.filter(username=request.user.username)
    return render(request, 'clientdash.html', {'projects': projects})

@login_required(login_url='login')
def worker_dash(request):
    return render(request, 'workerdash.html')

@login_required(login_url='login')
def worker_detail(request):
    return render(request, 'worker_detail.html')

@login_required(login_url='login')
def client_detail(request):
    return render(request, 'client_detail.html')

@login_required(login_url='login')
def create_project(request):
    form = CreateProjectForm()
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.username = request.user
            post.save()
            messages.success(request, 'Project was created successfully')
            return redirect('createproject')
        else:
            messages.error(request, "Fill the form with correct end date and total work hours")
            return redirect('createproject')
    context = {'form': form}
    return render(request, 'create_project.html', context)