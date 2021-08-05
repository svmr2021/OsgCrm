from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from django.utils import timezone
from datetime import datetime, date


class User(AbstractUser):
    ADMIN = 'Admin'
    LEADER = 'Leader'
    ACCOUNTANT = 'Accountant'
    EMPLOYEE = 'Employee'
    TRAINEE = 'Стажер'
    TEACHER = 'Учитель'
    STUDENT = 'Ученик'
    USER_TYPE = [
        (ADMIN, 'Админ'),
        (LEADER, 'Руководство'),
        (ACCOUNTANT, 'Бухгалтерия'),
        (EMPLOYEE, 'Сотрудник'),
        (TRAINEE, 'Стажер'),
        (TEACHER, 'Учитель'),
        (STUDENT,'Студент'),
    ]

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=20)
    home_phone = models.CharField(max_length=20, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    birth_date = models.DateField(null=True, blank=True)
    birth_place = models.CharField(max_length=30, null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=30, choices=USER_TYPE)
    position = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    img = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    file = models.FileField(upload_to='profile_files/', null=True, blank=True,
                            validators=[
                                FileExtensionValidator(
                                    allowed_extensions=['pdf', 'doc'])])
    activity_coefficient = models.FloatField(null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role', 'email', 'is_staff']

    def __str__(self):
        return f'{self.username}'

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class Salary(models.Model):
    UZS, USD = 'UZS','USD'
    SALARY_TYPE = [
        (UZS, 'UZS'),
        (USD, 'USD'),
    ]
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    salary_type = models.CharField(max_length=3, choices=SALARY_TYPE)

    def __str__(self):
        return f'{self.user}'


class Attendance(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    day = models.CharField(max_length=15, default=datetime.today().strftime('%A'))
    month = models.CharField(max_length=15, default=datetime.today().strftime('%m'))
    status = models.BooleanField(default=False)
    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)
    is_late = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    # def __str__(self):
    #     return f'{self.user} {self.date}'


class Time(models.Model):
    date = models.ForeignKey('Attendance', models.CASCADE, related_name='time')
    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
    # def __str__(self):
    #     return f'{self.date}'


class Balance(models.Model):
    UZS, USD = 'UZS','USD'
    BALANCE_TYPE = [
        (UZS, 'UZS'),
        (USD, 'USD'),
    ]
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    amount = models.IntegerField()
    balance_type = models.CharField(max_length=3, choices=BALANCE_TYPE, default=UZS)


class StandUp(models.Model):
    # user = models.ForeignKey('User', on_delete=models.CASCADE)
    attendance = models.OneToOneField('Attendance', on_delete=models.CASCADE, null=True, blank=True)
    # question = models.ForeignKey('Question', on_delete=models.DO_NOTHING)
    # answer = models.JSONField()
    reason = models.CharField(max_length=100, null=True, blank=True)
    q1 = models.CharField(max_length=100, null=True, blank=True)
    q2 = models.CharField(max_length=100, null=True, blank=True)
    q3 = models.CharField(max_length=100, null=True, blank=True)
    q4 = models.CharField(max_length=100, null=True, blank=True)
    q5 = models.CharField(max_length=100, null=True, blank=True)
    answer = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)


class Question(models.Model):
    question = models.TextField(max_length=100)

    # type = models.CharField()
    def __str__(self):
        return f'{self.question}'


class SendSalary(models.Model):
    AWAITING, ACCEPTED, REJECTED = 'В ожидании',"Подвтвержден",'Отклонен'
    Salary, Prepayment, Penalty = 'Зарплата','Аванс','Штраф'
    STATUS = [
        (AWAITING, 'В ожидании'),
        (ACCEPTED, 'Подвтержден'),
        (REJECTED, 'Отклонен')
    ]
    SALARY_TYPE = [
        (Salary, 'Зарплата'),
        (Prepayment, 'Аванс'),
        (Penalty, 'Штраф'),
    ]
    UZS = 'UZS'
    USD = 'USD'
    PAYMENT_TYPE = [
        (UZS, 'UZS'),
        (USD, 'USD'),
    ]
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    reason = models.TextField(max_length=100,null=True,blank=True)
    type = models.CharField(max_length=10,choices=SALARY_TYPE,default='Salary')
    payment_type = models.CharField(max_length=10,choices=PAYMENT_TYPE,null=True,blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='AWAITING')
    is_finished = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)