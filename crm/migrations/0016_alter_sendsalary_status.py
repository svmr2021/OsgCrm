# Generated by Django 3.2.5 on 2021-08-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0015_alter_sendsalary_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendsalary',
            name='status',
            field=models.CharField(choices=[('В ожидании', 'В ожидании'), ('Подвтвержден', 'Подвтержден'), ('Отклонен', 'Отклонен')], default='В ожидании', max_length=15),
        ),
    ]
