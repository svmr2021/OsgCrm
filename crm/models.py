from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from django.utils import timezone


class User(AbstractUser):
    ADMIN = 'Admin'
    LEADER = 'Leader'
    ACCOUNTANT = 'Accountant'
    EMPLOYEE = 'Employee'

    USER_TYPE = [
        (ADMIN,'Admin'),
        (LEADER,'Leader'),
        (ACCOUNTANT,'Accountant'),
        (EMPLOYEE,'Employee')
    ]

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30,unique=True)
    #firstname = models.CharField(max_length=30)
    #lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    start_date = models.DateTimeField(default=timezone.now)
    birth_date = models.DateField(null=True,blank=True)
    #is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    role = models.CharField(max_length=30,choices=USER_TYPE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name','role','email']

    def __str__(self):
        return f'{self.username}'


class Salary(models.Model):
    SUM = 'Sum'
    USD = 'Usd'
    SALARY_TYPE = [
        (SUM,'UZS'),
        (USD,'USD'),
    ]
    user = models.ForeignKey('User',on_delete=models.DO_NOTHING)
    amount = models.PositiveIntegerField()
    salary_type = models.CharField(max_length=3,choices=SALARY_TYPE)

    def __str__(self):
        return f'{self.user}'


class Attendance(models.Model):
    user = models.ForeignKey('User',on_delete=models.DO_NOTHING)
    data = models.DateField(null=True,blank=True)
    time_in = models.DateTimeField(null=True,blank=True)
    time_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user}'


class Balance(models.Model):
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    amount = models.IntegerField()


class StandUp(models.Model):
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    questions = models.ForeignKey('Questions',on_delete=models.DO_NOTHING)


class Questions(models.Model):
    question = models.TextField(max_length=100)

    def __str__(self):
        return f'{self.question}'