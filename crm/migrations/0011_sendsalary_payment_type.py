# Generated by Django 3.2.5 on 2021-08-05 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_alter_balance_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendsalary',
            name='payment_type',
            field=models.CharField(blank=True, choices=[('Sum', 'UZS'), ('Usd', 'USD')], max_length=10, null=True),
        ),
    ]