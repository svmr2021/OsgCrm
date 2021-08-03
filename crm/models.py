from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from django.utils import timezone
from datetime import datetime, date


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
    img = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    activity_coefficient = models.FloatField(null=True,blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role', 'email', 'is_staff']

    def __str__(self):
        return f'{self.username}'

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


    def get_activity_coefficient(self):
        dates = Attendance.objects.all().filter(user=self)
        working_minutes = 480
        days = 0
        total = 0
        for i in dates:
            days += 1
            times = Time.objects.filter(date = i)
            for time in times:
                datetime1 = datetime.combine(date.today(), time.time_out)
                datetime2 = datetime.combine(date.today(), time.time_in)
                time_elapsed = datetime1 - datetime2
                delta = time_elapsed.total_seconds()
                minutes = int(delta//60)
                total += minutes
        total_working_minutes = working_minutes * days

        try:
            value = (total * 100) / total_working_minutes
            formatted_string = "{:.2f}".format(value)
            self.activity_coefficient = formatted_string
            return  self.save()
        except:
            self.activity_coefficient = 0
            return  self.save()


class Salary(models.Model):
    SUM = 'Sum'
    USD = 'Usd'
    SALARY_TYPE = [
        (SUM, 'UZS'),
        (USD, 'USD'),
    ]
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    salary_type = models.CharField(max_length=3, choices=SALARY_TYPE)

    def __str__(self):
        return f'{self.user}'


class Attendance(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    day = models.CharField(max_length=15,default=datetime.today().strftime('%A'))
    month = models.CharField(max_length=15,default=datetime.today().strftime('%m'))
    status = models.BooleanField(default=False)
    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)
    finished = models.BooleanField(default=False)
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
    SUM = 'Sum'
    USD = 'Usd'
    BALANCE_TYPE = [
        (SUM, 'UZS'),
        (USD, 'USD'),
    ]
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    amount = models.IntegerField()
    balance_type = models.CharField(max_length=3, choices=BALANCE_TYPE,default=SUM)


class StandUp(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    #question = models.ForeignKey('Question', on_delete=models.DO_NOTHING)
    #answer = models.JSONField()
    reason = models.CharField(max_length=100,null=True,blank=True)
    q1 = models.CharField(max_length=100,null=True,blank=True)
    q2 = models.CharField(max_length=100, null=True, blank=True)
    q3= models.CharField(max_length=100, null=True, blank=True)
    q4 = models.CharField(max_length=100, null=True, blank=True)
    q5 = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    question = models.TextField(max_length=100)
    #type = models.CharField()
    def __str__(self):
        return f'{self.question}'


class SendSalary(models.Model):
    STATUS = [
        ('AWAITING','В ожидании'),
        ('ACCEPTED','Принят'),
        ('REJECTED','Отклонен')
    ]
    user = models.ForeignKey("User",on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    status = models.CharField(max_length=10,choices=STATUS,default='AWAITING')