# Generated by Django 2.2.5 on 2020-03-31 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_auto_20200329_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(verbose_name='End Date* (YYYY-MM-DD)'),
        ),
    ]
