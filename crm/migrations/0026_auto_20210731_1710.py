# Generated by Django 3.2.5 on 2021-07-31 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0025_alter_attendance_time_in'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='data',
            new_name='date',
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.TimeField(auto_now_add=True)),
                ('time_out', models.TimeField(blank=True, null=True)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crm.attendance')),
            ],
        ),
    ]
