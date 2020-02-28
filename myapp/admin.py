from django.contrib import admin
from .models import Admin, Client, Worker, Project_Status, Project, Worker_status

class Project_status_Admin(admin.ModelAdmin):
    list_display =['id','status']

class Worker_status_Admin(admin.ModelAdmin):
    list_display =['id','status']

# Register your models here.
admin.site.register(Admin)
admin.site.register(Client)
admin.site.register(Worker)
admin.site.register(Project_Status, Project_status_Admin)
admin.site.register(Project)
admin.site.register(Worker_status, Worker_status_Admin)