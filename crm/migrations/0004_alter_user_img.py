# Generated by Django 3.2.5 on 2021-07-30 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_alter_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, default='assets/images/avatar.png', null=True, upload_to='profile_images/'),
        ),
    ]
