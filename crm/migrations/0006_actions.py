# Generated by Django 3.2.5 on 2021-08-05 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_alter_exchangerate_one_dollar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('Create_user', 'Добавление сотрудника'), ('Edit_user', 'Изменение сотрудника'), ('Add_salary', 'Добавление зарплаты'), ('Edit_salary', 'Изменение зарплаты'), ('Send_salary', 'Отправка зарплаты'), ('Send_prepayment', 'Отправка премии'), ('Send_penalty', 'Отправка штрафа')], max_length=30)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Client', to=settings.AUTH_USER_MODEL)),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Executor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
