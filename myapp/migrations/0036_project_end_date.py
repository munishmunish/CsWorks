# Generated by Django 2.2.5 on 2020-04-02 07:29

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_project_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, validators=[myapp.models.validate_date_not_in_past]),
        ),
    ]
