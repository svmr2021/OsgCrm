from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from django.utils import timezone
from datetime import datetime


class User(AbstractUser):
    ADMIN = 'Admin'
    LEADER = 'Leader'
    ACCOUNTANT = 'Accountant'
    EMPLOYEE = 'Employee'

    USER_TYPE = [
        (ADMIN, 'Админ'),
        (LEADER, 'Руководство'),
        (ACCOUNTANT, 'Бухгалтерия'),
        (EMPLOYEE, 'Сотрудник')
    ]

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=20)
    date_joined = models.DateTimeField(default=timezone.now)
    birth_date = models.DateField(null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=30, choices=USER_TYPE)
    position = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    img = models.ImageField(upload_to='profile_images/',default='default.JPG', null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role', 'email', 'is_staff']

    def __str__(self):
        return f'{self.username}'

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class Salary(models.Model):
    SUM = 'Sum'
    USD = 'Usd'
    SALARY_TYPE = [
        (SUM, 'UZS'),
        (USD, 'USD'),
    ]
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    amount = models.PositiveIntegerField()
    salary_type = models.CharField(max_length=3, choices=SALARY_TYPE)

    def __str__(self):
        return f'{self.user}'


class Attendance(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    day = models.CharField(max_length=15,default=datetime.today().strftime('%A'))
    status = models.BooleanField(default=False)

    # def __str__(self):
    #     return f'{self.user} {self.date}'


class Time(models.Model):
    date = models.ForeignKey('Attendance',models.CASCADE,related_name='time')
    time_in = models.TimeField(null=True,blank=True)
    time_out = models.TimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
    # def __str__(self):
    #     return f'{self.date}'


class Balance(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    amount = models.IntegerField()


class StandUp(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    questions = models.ForeignKey('Question', on_delete=models.DO_NOTHING)


class Question(models.Model):
    question = models.TextField(max_length=100)

    def __str__(self):
        return f'{self.question}'
