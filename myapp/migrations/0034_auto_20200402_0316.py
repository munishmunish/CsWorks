# Generated by Django 2.2.5 on 2020-04-02 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_auto_20200402_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='point_per_hour',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='status',
        ),
        migrations.RemoveField(
            model_name='project',
            name='total_work_hours',
        ),
    ]
