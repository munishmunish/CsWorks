# Generated by Django 2.2.5 on 2020-04-02 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0050_remove_project_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='point_per_hour',
        ),
        migrations.RemoveField(
            model_name='project',
            name='total_work_hours',
        ),
    ]