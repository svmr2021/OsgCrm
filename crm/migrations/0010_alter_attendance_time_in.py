# Generated by Django 3.2.5 on 2021-07-31 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_alter_attendance_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='time_in',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
