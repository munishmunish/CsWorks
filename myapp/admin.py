from django.contrib import admin
from .models import Project_Status, Project, Skills

class Project_status_Admin(admin.ModelAdmin):
    list_display =['id','status']

class Project_Admin(admin.ModelAdmin):
    list_display = ['username', 'title']
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        instance.username = user
        instance.save()
        form.save_m2m()
        return instance

# class Payment_Admin(admin.ModelAdmin):
#     list_display = ['total_work_hours', 'point_per_hour']


# admin.site.register(Payment, Payment_Admin)
admin.site.register(Skills)
admin.site.register(Project_Status, Project_status_Admin)
admin.site.register(Project, Project_Admin)
# admin.site.register(Worker_status, Worker_status_Admin)