# Generated by Django 2.2.5 on 2020-03-31 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_auto_20200331_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(validators=[myapp.models.validate_date_not_in_past]),
        ),
        migrations.AlterField(
            model_name='project',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]