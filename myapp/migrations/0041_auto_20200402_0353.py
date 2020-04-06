# Generated by Django 2.2.5 on 2020-04-02 07:53

import datetime
from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_auto_20200402_0353'),
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
            field=models.DateField(default=datetime.date.today),
        ),
    ]