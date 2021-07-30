from rest_framework import serializers
from crm.models import User


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
    class Meta:
        model = Attendance
        fields = "__all__"


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


