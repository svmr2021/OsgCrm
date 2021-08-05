# Generated by Django 3.2.5 on 2021-08-05 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0018_auto_20210805_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendsalary',
            name='status',
            field=models.CharField(choices=[('AWAITING', 'В ожидании'), ('ACCEPTED', 'Подвтержден'), ('REJECTED', 'Отклонен')], default='AWAITING', max_length=15),
        ),
        migrations.AlterField(
            model_name='sendsalary',
            name='type',
            field=models.CharField(choices=[('Salary', 'Зарплата'), ('Prepayment', 'Аванс'), ('Penalty', 'Штраф')], max_length=10),
        ),
    ]
