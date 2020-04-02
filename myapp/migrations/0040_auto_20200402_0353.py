# Generated by Django 2.2.5 on 2020-04-02 07:53

from django.db import migrations, models
import django.utils.timezone
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0039_auto_20200402_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, validators=[myapp.models.validate_date_not_in_past]),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
