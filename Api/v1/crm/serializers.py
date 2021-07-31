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
    times = TimeSerializer(source='time', many=True)

    class Meta:
        model = Attendance
        fields = ['user','times','status']

    def create(self, validated_data):
        today = datetime.today().strftime('%Y-%m-%d')
        user = validated_data['user']
        time = validated_data.pop('time')
        try:
            obj = Attendance.objects.get(user=user,date=today)
            try:
                time = Time.objects.get(date=obj)
                print(time)
            except:
                time = Time(date=obj)
                time.save()
            if not obj.status:
                if time.time_in or time.time_out is not None:
                    time.time_in = (datetime.now().strftime('%H:%M'))
                else:
                    time.time_in = (datetime.now().strftime('%H:%M'))
                obj.status = True
                time.save()
            elif obj.status:
                if time.time_in or time.time_out is not None:
                    time.time_out = (datetime.now().strftime('%H:%M'))
                else:
                    time.time_out = (datetime.now().strftime('%H:%M'))
                time.save()
        except:
            obj = Attendance(**validated_data)
            obj.save()
        return obj

    def to_representation(self, instance):
        instance = super(AttendanceSerializer,self).to_representation(instance)
        return instance

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



