from rest_framework import serializers, status
from rest_framework.response import Response
from datetime import datetime
from crm.models import User
from crm.models import Time


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ['time_in','time_out']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


from crm.models import Salary


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = "__all__"


from crm.models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    times = TimeSerializer(source='time',many=True)

    class Meta:
        model = Attendance
        fields = ['user','date','times','status']


class AttendanceCreateSerializer(serializers.ModelSerializer):
    times = TimeSerializer(source='time')

    class Meta:
        model = Attendance
        fields = ['user','times','status']

    def create(self, validated_data):
        today = datetime.today().strftime('%Y-%m-%d')
        user = validated_data.pop('user')

        date, created = Attendance.objects.get_or_create(user=user,date=today)
        time, create = Time.objects.get_or_create(date=date,status=False)

        if not date.status:
            time.time_in = datetime.now().strftime('%H:%M')
            time.save()
            date.status = True
            date.save()
        elif date.status:
            time.time_out = datetime.now().strftime('%H:%M')
            time.status = True
            time.save()

            date.status = False
            date.save()
        return date


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


from crm.models import Questions


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = "__all__"



