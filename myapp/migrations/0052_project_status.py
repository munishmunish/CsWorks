# Generated by Django 2.2.5 on 2020-04-02 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0051_auto_20200402_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_status_set', to='myapp.Project_Status'),
        ),
    ]