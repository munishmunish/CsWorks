"""CsWorks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'myapp/', include('myapp.urls')),
    path(r'', views.home, name='home'),
    path(r'about/', views.about, name='about'),
    path(r'help/', views.help, name='help'),
    path(r'logout/', views.logoutUser, name='logout'),
    path(r'login/', views.loginUser, name='login'),
    path(r'register/', views.register, name='register'),
    path(r'logout/', views.logout, name='logout'),
    path(r'login/admindash', views.admin_dash, name='admindash'),
    path(r'login/clientdash', views.client_dash, name='clientdash'),
    path(r'login/workerdash', views.worker_dash, name='workerdash'),

]
