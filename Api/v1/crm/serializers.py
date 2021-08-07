import array

from rest_framework import serializers, status
from rest_framework.response import Response
from datetime import datetime
from crm.models import User
from crm.models import Time
from pprint import pprint
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from crm.models import Debt, Action, ExchangeRate
from crm.logfile import logfile


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ['time_in', 'time_out']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True, required=False)

    class Meta:
        model = User
        fields = ['password',
                  'first_name',
                  'last_name',
                  'middle_name',
                  'email',
                  'phone',
                  'birth_place',
                  'home_phone',
                  'birth_date',
                  'username',
                  'position',
                  'role',
                  'img',
                  'file']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        current_user = self.context.get('request').user
        logfile(current_user, 'Create_user', validated_data)

        return user

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        if password is not None:
            password = validated_data.pop('password')
            instance.set_password(password)

        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.middle_name = validated_data.get('middle_name')
        instance.email = validated_data.get('email')
        instance.phone = validated_data.get('phone')
        instance.birth_date = validated_data.get('birth_date')
        instance.username = validated_data.get('username')
        instance.position = validated_data.get('position')
        instance.role = validated_data.get('role')

        instance.image = validated_data.get('img')

        instance.save()

        current_user = self.context.get('request').user
        logfile(creator=current_user, type='Edit_user', validated_data=validated_data)
        return instance


from crm.models import Salary


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = "__all__"

    def create(self, validated_data):
        salary = Salary(**validated_data)
        user = validated_data.get('user')
        salary_type = validated_data.get('salary_type')
        if user and salary_type is not None:
            balance = Balance.objects.create(user=user, balance_type=salary_type)
            balance.save()
            salary.save()

        creator = self.context.get('request').user
        if creator is not None:
            logfile(creator=creator, type='Add_salary', validated_data=validated_data)
        return salary

    def update(self, instance, validated_data):
        salary = validated_data.get('amount')
        salary_type = validated_data.get('salary_type')
        balance = instance.user.balance
        if balance.amount != 0:
            raise ValidationError('Невозможно изменить зарплату. Обнулите баланс')
        else:
            instance.amount = salary
            instance.salary_type = salary_type
            instance.save()

            creator = self.context.get('request').user
            if creator is not None:
                validated_data['user'] = instance.user
                logfile(creator=creator, type='Edit_salary', validated_data=validated_data)
        return instance


from crm.models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    # times = TimeSerializer(source='time',many=True)

    class Meta:
        model = Attendance
        fields = ['id',
                  'user',
                  'date',
                  'time_in',
                  'time_out',
                  'day',
                  'status',
                  'finished']


class AttendanceCreateSerializer(serializers.ModelSerializer):
    # times = TimeSerializer(source='time')
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Attendance
        fields = ['id',
                  'user',
                  'time_in',
                  'time_out',
                  'status',
                  'is_late',
                  'finished']
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        now = datetime.now()
        today10am = now.replace(hour=10, minute=0, second=0, microsecond=0)
        today = datetime.today().strftime('%Y-%m-%d')
        user = self.context.get('request').user
        date, created = Attendance.objects.get_or_create(user=user, date=today)
        standup = StandUp.objects.filter(attendance=date).exists()
        if not date.finished:
            if not date.status:
                if now > today10am:
                    date.is_late = True
                date.time_in = datetime.now().strftime('%H:%M')
                date.status = True
                date.save()
            elif date.status and standup:
                date.time_out = datetime.now().strftime('%H:%M')
                date.status = False
                date.finished = True
                date.save()
            else:
                raise ValidationError('Пожалуйста заполните опрос!')
        return date

    # def create(self, validated_data):
    #     today = datetime.today().strftime('%Y-%m-%d')
    #     user = validated_data.pop('user')
    #
    #     date, created = Attendance.objects.get_or_create(user=user,date=today)
    #     time, create = Time.objects.get_or_create(date=date,status=False)
    #
    #     if not date.status:
    #         time.time_in = datetime.now().strftime('%H:%M')
    #         time.save()
    #         date.status = True
    #         date.save()
    #     elif date.status:
    #         time.time_out = datetime.now().strftime('%H:%M')
    #         time.status = True
    #         time.save()
    #
    #         date.status = False
    #         date.save()
    #
    #         user.get_activity_coefficient()
    #         user.save()
    #     return date


from crm.models import Balance


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = "__all__"


from crm.models import StandUp


class StandUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandUp
        fields = "__all__"
        extra_kwargs = {
            'user': {'required': False}
        }

    def validate_reason(self, attrs):
        now = datetime.now()
        today10am = now.replace(hour=10, minute=0, second=0, microsecond=0)
        if now > today10am:
            reason = attrs.get('reason')
            if reason is None:
                raise ValidationError('Reason field is required!Length should be not less than 10')
        return attrs

    def create(self, validated_data):
        today = datetime.today().strftime('%Y-%m-%d')
        user = self.context.get('request').user
        # try:
        #     standup = StandUp.objects.get(user=user, date=today)
        # except:
        #     standup = StandUp(**validated_data)
        # standup.finished = True
        # standup.save()
        attendance = Attendance.objects.filter(date=today).exists()
        if attendance:
            attendance = Attendance.objects.get(date=today)
            standup = StandUp.objects.filter(attendance=attendance).exists()
            if standup:
                standup.finished = True
                standup.save()
            else:
                standup = StandUp(**validated_data)
                standup.finished = True
                standup.save()
            return standup
        else:
            return 1

    def update(self, instance, validated_data):
        answer = validated_data.get('answer')
        if instance is None:
            raise ValidationError('Вы не заполнили опрос!')
        elif answer is not None:
            instance.answer = answer
            instance.save()
        return instance


from crm.models import Question


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


from crm.models import SendSalary


class SendSalarySerializer(serializers.ModelSerializer):
    # status = serializers.HiddenField(default='AWAITING')

    class Meta:
        model = SendSalary
        fields = "__all__"

    def create(self, validated_data):
        executor = self.context.get('request').user
        client = validated_data.get('user')
        type = validated_data.get('type')

        send_salary = SendSalary(**validated_data)
        send_salary.save()
        try:
            if type == 'Salary':
                action = Action.objects.create(executor=executor, client=client, type='Send_salary')
                action.save()
            elif type == 'Prepayment':
                action = Action.objects.create(executor=executor, client=client, type='Send_prepayment')
                action.save()
            elif type == 'Penalty':
                action = Action.objects.create(executor=executor, client=client, type='Send_penalty')
                action.save()
        except:
            pass

        creator = self.context.get('request').user
        if creator is not None:
            logfile(creator=creator, type='Send_salary', validated_data=validated_data)
        return send_salary


class SendSalaryEditSerializer(serializers.ModelSerializer):
    # status = serializers.HiddenField(default='AWAITING')
    class Meta:
        model = SendSalary
        fields = [
            'status'
        ]

    def update(self, instance, validated_data):
        if not instance.is_finished:
            today = datetime.today().strftime('%Y-%m-%d')
            instance.status = validated_data.get('status')
            instance.is_finished = True
            instance.save()
            exchange = ExchangeRate.objects.get(date=today)
            balance = instance.user.balance
            if instance.status == 'ACCEPTED':
                if instance.type == 'Salary' or instance.type == 'Penalty':
                    if instance.payment_type == 'UZS' and instance.user.salary.salary_type == 'UZS':
                        balance.amount -= instance.amount
                        balance.save()
                    elif instance.payment_type == 'UZS' and instance.user.salary.salary_type == 'USD':
                        amount = instance.amount / exchange.one_dollar
                        balance.amount -= amount
                        balance.save()
                    elif instance.payment_type == 'USD' and instance.user.salary.salary_type == 'UZS':
                        amount = instance.amount * exchange.one_dollar
                        balance.amount -= amount
                        balance.save()
                    elif instance.payment_type == 'USD' and instance.user.salary.salary_type == 'USD':
                        balance.amount -= instance.amount
                        balance.save()
                elif instance.type == 'Prepayment':
                    if instance.payment_type == 'UZS' and instance.user.salary.salary_type == 'UZS':
                        balance.amount += instance.amount
                        balance.save()
                    elif instance.payment_type == 'UZS' and instance.user.salary.salary_type == 'USD':
                        amount = instance.amount / exchange.one_dollar
                        balance.amount += amount
                        balance.save()
                    elif instance.payment_type == 'USD' and instance.user.salary.salary_type == 'UZS':
                        amount = instance.amount * exchange.one_dollar
                        balance.amount += amount
                        balance.save()
                    elif instance.payment_type == 'USD' and instance.user.salary.salary_type == 'USD':
                        balance.amount += instance.amount
                        balance.save()

                validated_data['instance'] = instance
                creator = self.context.get('request').user
                logfile(creator=creator, type='Accept_salary', validated_data=validated_data)
            elif instance.status == 'REJECTED':
                validated_data['instance'] = instance
                creator = self.context.get('request').user
                logfile(creator=creator, type='Decline_salary', validated_data=validated_data)
        return instance


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = "__all__"


class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = "__all__"


from crm.models import Action


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = "__all__"
