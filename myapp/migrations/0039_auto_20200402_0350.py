# Generated by Django 2.2.5 on 2020-04-02 07:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0038_auto_20200402_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
