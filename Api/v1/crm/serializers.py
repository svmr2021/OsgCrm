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
    password = serializers.CharField(min_length=8, write_only=True)
    img = serializers.ImageField(default='default.JPG')
    class Meta:
        model = User
        fields = ['id','password','first_name','last_name','email','username','position','role','img','activity_coefficient']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def to_representation(self, instance):
        instance = super(UserSerializer,self).to_representation(instance)
        pprint(instance)
        id = instance['id']
        user = User.objects.get(id=id)
        user.get_activity_coefficient()
        dates = Attendance.objects.all().filter(user=user)
        try:
            times = Time.objects.all().filter(date=dates)
            pprint(times)
        except Exception as e:
            print(e)

        #pprint(dates)
        return instance


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
        fields = ['user','date','times','day','status']


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


from crm.models import Question


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"



