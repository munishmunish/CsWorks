# Generated by Django 2.2.5 on 2020-02-28 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200228_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_status',
            name='id',
            field=models.PositiveSmallIntegerField(choices=[('Pending', '1'), ('Approved', '2'), ('Declined', '3'), ('Completed', '4')], primary_key=True, serialize=False),
        ),
    ]
