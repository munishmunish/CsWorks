# Generated by Django 2.2.5 on 2020-04-02 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0043_auto_20200402_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.ForeignKey(default='PENDING', on_delete=django.db.models.deletion.CASCADE, related_name='project', to='myapp.Project_Status'),
        ),
    ]