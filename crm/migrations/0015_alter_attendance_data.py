# Generated by Django 3.2.5 on 2021-07-31 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_alter_attendance_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='data',
            field=models.DateField(default='2021-07-31'),
        ),
    ]
