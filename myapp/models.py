from datetime import date

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField



class Project_Status(models.Model):

    STATUS_CHOICE = [
        ('PENDING', 'PENDING'),
        ('APPROVED', 'APPROVED'),
        ('DECLINED', 'DECLINED'),
        ('COMPLETED', 'COMPLETED')
    ]
    id = models.PositiveSmallIntegerField(primary_key=True)
    status = models.CharField(max_length=20, unique=True, choices=STATUS_CHOICE, default='PENDING')

    def __str__(self):
        if self.status:
            return self.status

def validate_date_not_in_past(value):
    if value <= date.today():
        raise ValidationError('Date cannot be in the past')


class Project(models.Model):
    username = models.ForeignKey(User, to_field="username", related_name='project', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500)
    start_date = models.DateField(default=date.today, auto_now=False, blank=False)
    end_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True, validators=[validate_date_not_in_past])
    status = models.ForeignKey(Project_Status, default=1, related_name='project', on_delete=models.CASCADE)
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

class Worker_Status(models.Model):

    STATUS_CHOICE = [
        ('PENDING', 'PENDING'),
        ('APPROVED', 'APPROVED'),
        ('DECLINED', 'DECLINED'),
    ]
    id = models.PositiveSmallIntegerField(primary_key=True)
    status = models.CharField(max_length=20, unique=True, choices=STATUS_CHOICE, default='PENDING')

    def __str__(self):
        if self.status:
            return self.status

class Worker_Request(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    title = models.ForeignKey(Project, to_field="title", related_name="worker_request", on_delete=models.CASCADE)

    def __str__(self):
        if self.title:
            return self.title

class Worker(models.Model):
    username = models.ForeignKey(User, to_field="username", related_name='worker_username', on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True, blank=False, null=False)
    application_date = models.DateField(default=date.today, auto_now=False, blank=False)
    status = models.ForeignKey(Worker_Status, default=1, related_name='worker', on_delete=models.CASCADE)

    def __str__(self):
        if self.username:
            return str(self.username)