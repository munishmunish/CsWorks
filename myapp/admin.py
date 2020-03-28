from django.contrib import admin
from .models import Project_Status, Project, Payment

class Project_status_Admin(admin.ModelAdmin):
    list_display =['id','status']

class Project_Admin(admin.ModelAdmin):
    list_display = ['username', 'title']

class Payment_Admin(admin.ModelAdmin):
    list_display = ['total_work_hours', 'point_per_hour']

# Register your models here.

admin.site.register(Payment, Payment_Admin)
admin.site.register(Project_Status, Project_status_Admin)
admin.site.register(Project, Project_Admin)
# admin.site.register(Worker_status, Worker_status_Admin)