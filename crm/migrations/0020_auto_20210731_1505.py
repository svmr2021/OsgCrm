# Generated by Django 3.2.5 on 2021-07-31 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0019_alter_attendance_time_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='data',
            field=models.DateField(default='2021-07-31', unique=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_in',
            field=models.TimeField(default='15-05'),
        ),
    ]
