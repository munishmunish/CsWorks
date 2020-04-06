from django.contrib import admin
from .models import Project_Status, Project, Skills, Worker_Status, Worker, Worker_Request

class Project_status_Admin(admin.ModelAdmin):
    readonly_fields = ('id', 'status')
    list_display = ['id', 'status']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class Worker_status_Admin(admin.ModelAdmin):
    readonly_fields = ('id', 'status')
    list_display = ['id', 'status']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class Project_Admin(admin.ModelAdmin):
    list_display = ['username', 'title', 'start_date', 'end_date', 'status', 'total_work_hours', 'point_per_hour']
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        instance.username = user
        instance.save()
        form.save_m2m()
        return instance

class Worker_Admin(admin.ModelAdmin):
    list_display = ['username', 'phone_number', 'status']
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        instance.username = user
        instance.save()
        form.save_m2m()
        return instance

admin.site.register(Skills)
admin.site.register(Project_Status, Project_status_Admin)
admin.site.register(Project, Project_Admin)
admin.site.register(Worker, Worker_Admin)
admin.site.register(Worker_Status, Worker_status_Admin)
admin.site.register(Worker_Request)
# admin.site.register(Worker_status, Worker_status_Admin)