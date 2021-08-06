# Generated by Django 3.2.5 on 2021-08-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_action_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='client',
        ),
        migrations.AlterField(
            model_name='action',
            name='type',
            field=models.CharField(choices=[('Create_user', 'Добавление сотрудника'), ('Edit_user', 'Изменение сотрудника'), ('Add_salary', 'Добавление зарплаты'), ('Edit_salary', 'Изменение зарплаты'), ('Send_salary', 'Отправка зарплаты'), ('Send_prepayment', 'Отправка премии'), ('Send_penalty', 'Отправка штрафа'), ('Accept_salary', 'Принять зарплату'), ('Accept_prepayment', 'Принять аванс'), ('Accept_penalty', 'Принять штраф')], max_length=30),
        ),
    ]
