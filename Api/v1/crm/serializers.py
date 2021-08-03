from rest_framework import serializers, status
from rest_framework.response import Response
from datetime import datetime
from crm.models import User
from crm.models import Time
from pprint import pprint

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ['time_in','time_out']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True, required=False)


    class Meta:
        model = User
        fields = ['password', 'first_name', 'last_name', 'middle_name', 'email',
                  'phone', 'birth_date', 'username', 'position', 'role', 'img']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        try:
            password = validated_data.pop('password')
            if len(password) > 1:
                instance.set_password(password)
        except:
            pass
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.middle_name = validated_data['middle_name']
        instance.email = validated_data['email']
        instance.phone = validated_data['phone']
        instance.birth_date = validated_data['birth_date']
        instance.username = validated_data['username']
        instance.position = validated_data['position']
        instance.role = validated_data['role']
        instance.image = validated_data['img']
        instance.activity_coefficient = validated_data['activity_coefficient']

        instance.save()
        return instance

from crm.models import Salary


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = "__all__"


from crm.models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    #times = TimeSerializer(source='time',many=True)

    class Meta:
        model = Attendance
        fields = ['user','date','time_in','time_out','day','status','finished']


class AttendanceCreateSerializer(serializers.ModelSerializer):
    #times = TimeSerializer(source='time')

    class Meta:
        model = Attendance
        fields = ['user','time_in','time_out','status','finished']
        extra_kwargs = {
            'user': {'required':False}
        }

    def create(self, validated_data):
        today = datetime.today().strftime('%Y-%m-%d')
        user = self.context['request'].user
        date, created = Attendance.objects.get_or_create(user=user,date=today)
        if not date.finished:
            if not date.status:
                date.time_in = datetime.now().strftime('%H:%M')
                date.status = True
                date.save()
            elif date.status:
                date.time_out = datetime.now().strftime('%H:%M')
                date.status = False
                date.finished = True
                date.save()
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


from crm.models import Question


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


from crm.models import SendSalary


class SendSalarySerializer(serializers.ModelSerializer):
    status = serializers.HiddenField(default='AWAITING')
    class Meta:
        model = SendSalary
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        send_salary = SendSalary(**validated_data)
        send_salary.save()

        return send_salary
