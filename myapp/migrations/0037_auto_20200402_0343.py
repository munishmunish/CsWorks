# Generated by Django 2.2.5 on 2020-04-02 07:43

import datetime
from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0036_project_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, null=True, validators=[myapp.models.validate_date_not_in_past]),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 2, 3, 43, 33, 55507)),
        ),
    ]
