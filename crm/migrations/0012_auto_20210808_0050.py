# Generated by Django 3.2.5 on 2021-08-07 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_auto_20210807_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='standup',
            name='is_send',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default='2021-08-08'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='day',
            field=models.CharField(default='Sunday', max_length=15),
        ),
    ]
