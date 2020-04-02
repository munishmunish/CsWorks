from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
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

def validate_date_not_in_past(value):
    if value <= timezone.now():
        raise ValidationError('Date cannot be in the past')


class Project(models.Model):
    username = models.ForeignKey(User, to_field="username", related_name='project', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500)
    start_date = models.DateTimeField(default=timezone.now, auto_now=False, blank=False)
    end_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True,
                                    validators=[validate_date_not_in_past])
    status = models.ForeignKey(Project_Status, default='PENDING', related_name='project', on_delete=models.CASCADE)
    total_work_hours = models.PositiveIntegerField(default=1, null=False, blank=False)
    point_per_hour = models.PositiveIntegerField(default=2, null=False, blank=False)

    def __str__(self):
        if self.title:
            return self.title

class Skills(models.Model):
    skill = models.CharField(max_length=100, blank=False, unique=True)

    def __str__(self):
        if self.skill:
            return self.skill