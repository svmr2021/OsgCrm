# Generated by Django 3.2.5 on 2021-07-31 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0026_auto_20210731_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='time_in',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='time_out',
        ),
    ]
