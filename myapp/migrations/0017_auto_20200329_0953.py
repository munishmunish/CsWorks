# Generated by Django 2.2.5 on 2020-03-29 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20200329_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='payment',
        ),
        migrations.AddField(
            model_name='project',
            name='point_per_hour',
            field=models.PositiveIntegerField(default=2),
        ),
        migrations.AddField(
            model_name='project',
            name='project_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='project',
            name='total_work_hours',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.ForeignKey(default='PENDING', on_delete=django.db.models.deletion.CASCADE, related_name='project', to='myapp.Project_Status'),
        ),
    ]
