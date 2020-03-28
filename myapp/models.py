from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# class Client(models.Model):
#     username = models.EmailField(max_length=200, unique=True)
#     first_name = models.CharField(max_length=200)
#     middle_name = models.CharField(max_length=200, null=True, blank=True)
#     last_name = models.CharField(max_length=200)
#     phone_number = models.IntegerField()
#     password = models.CharField(max_length=100)
#
#     def __str__(self):
#         if self.username:
#             return self.username
#         return super().__str__()
#
# class Worker_status(models.Model):
#
#     STATUS_CHOICE = [
#         ('PENDING', 'PENDING'),
#         ('APPROVED', 'APPROVED'),
#         ('DECLINED', 'DECLINED'),
#     ]
#     id = models.PositiveSmallIntegerField(primary_key=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='PENDING')
#
#     def __str__(self):
#         if self.status:
#             return self.status
#
# class Worker(models.Model):
#     username = models.EmailField(max_length=200, unique=True)
#     first_name = models.CharField(max_length=200)
#     middle_name = models.CharField(max_length=200, null=True, blank=True)
#     last_name = models.CharField(max_length=200)
#     phone_number = models.IntegerField()
#     password = models.CharField(max_length=100)
#     status = models.ForeignKey(Worker_status, related_name='worker', on_delete=models.CASCADE)
#
#     def __str__(self):
#         if self.username:
#             return self.username
#
# class Admin(models.Model):
#     username = models.EmailField(max_length=150, unique=True)
#     first_name = models.CharField(max_length=200)
#     middle_name = models.CharField(max_length=200, null=True, blank=True)
#     last_name = models.CharField(max_length=200)
#     password = models.CharField(max_length=100)
#
#     def __str__(self):
#         if self.username:
#             return self.username
#         return super().__str__()

class Project_Status(models.Model):

    STATUS_CHOICE = [
        ('PENDING', 'PENDING'),
        ('APPROVED', 'APPROVED'),
        ('DECLINED', 'DECLINED'),
        ('COMPLETED', 'COMPLETED')
    ]
    id = models.PositiveSmallIntegerField(primary_key=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='PENDING')

    def __str__(self):
        if self.status:
            return self.status

class Payment(models.Model):
    total_work_hours = models.PositiveIntegerField(default=0, null=False, blank=False)
    point_per_hour = models.PositiveIntegerField(default=2, null=False, blank=False)

    def __str__(self):
        if self.total_work_hours and self.point_per_hour:
            return '%s %s' % (self.total_work_hours, self.point_per_hour)


class Project(models.Model):
    username = models.ForeignKey(User, to_field="username", related_name='project', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    status = models.ForeignKey(Project_Status, related_name='project', on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, default=0, related_name='project', on_delete=models.CASCADE)

    def __str__(self):
        if self.title:
            return self.title