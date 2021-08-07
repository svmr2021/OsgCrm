from rest_framework.generics import *
from rest_framework.permissions import *
from Api.v1.crm.serializers import *
from crm.models import *
from crm.permissions import *


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = (LeaderAdminAccess,)
    queryset = User.objects.all()


class UserEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = (AdminAccess,)
    queryset = User.objects.all()


class SalaryListView(ListAPIView):
    serializer_class = SalarySerializer
    permission_classes = (AdminAccess,)
    queryset = Salary.objects.all()


class SalaryCreateView(CreateAPIView):
    serializer_class = SalarySerializer
    permission_classes = (LeaderAccess,)
    queryset = Salary.objects.all()


class SalaryEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = SalarySerializer
    permission_classes = (LeaderAccess,)
    queryset = Salary.objects.all()


class AttendanceListView(ListAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = (AllowAny,)
    queryset = Attendance.objects.all()


class AttendanceCreateView(CreateAPIView):
    serializer_class = AttendanceCreateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Attendance.objects.all()


class AttendanceEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = (AdminAccess,)
    queryset = Attendance.objects.all()


class BalanceListView(ListAPIView):
    serializer_class = BalanceSerializer
    permission_classes = (AdminAccess,)
    queryset = Balance.objects.all()


class BalanceCreateView(CreateAPIView):
    serializer_class = BalanceSerializer
    permission_classes = (LeaderAccess,)
    queryset = Balance.objects.all()


class BalanceEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = BalanceSerializer
    permission_classes = (LeaderAccess,)
    queryset = Balance.objects.all()


class StandUpListView(ListAPIView):
    serializer_class = StandUpSerializer
    permission_classes = (AllowAny,)
    queryset = StandUp.objects.all()


class StandUpCreateView(CreateAPIView):
    serializer_class = StandUpSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = StandUp.objects.all()


class StandUpEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = StandUpSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = StandUp.objects.all()


class QuestionListView(ListAPIView):
    serializer_class = QuestionsSerializer
    permission_classes = (AllowAny,)
    queryset = Question.objects.all()


class QuestionCreateView(CreateAPIView):
    serializer_class = QuestionsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Question.objects.all()


class QuestionEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Question.objects.all()


class TimeListView(ListAPIView):
    serializer_class = TimeSerializer
    permission_classes = (AllowAny,)
    queryset = Time.objects.all()


class TimeCreateView(CreateAPIView):
    serializer_class = TimeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Time.objects.all()


class TimeEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = TimeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Time.objects.all()


class SendSalaryListView(ListAPIView):
    serializer_class = SendSalarySerializer
    permission_classes = (LeaderAccess,)
    queryset = SendSalary.objects.all()


class SendSalaryCreateView(CreateAPIView):
    serializer_class = SendSalarySerializer
    permission_classes = (LeaderAccess,)
    queryset = SendSalary.objects.all()


class SendSalaryEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = SendSalaryEditSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = SendSalary.objects.all()


class DebtListView(ListAPIView):
    serializer_class = DebtSerializer
    permission_classes = (LeaderAccess,)
    queryset = Debt.objects.all()


class DebtCreateView(CreateAPIView):
    serializer_class = DebtSerializer
    permission_classes = (AdminAccess,)
    queryset = Debt.objects.all()


class DebtEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = DebtSerializer
    permission_classes = (AdminAccess,)
    queryset = Debt.objects.all()


class ExchangeRateListView(ListAPIView):
    serializer_class = ExchangeRateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ExchangeRate.objects.all()


class ExchangeRateCreateView(CreateAPIView):
    serializer_class = ExchangeRateSerializer
    permission_classes = (AdminAccess,)
    queryset = ExchangeRate.objects.all()


class ExchangeRateEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExchangeRateSerializer
    permission_classes = (AdminAccess,)
    queryset = ExchangeRate.objects.all()


class ActionListView(ListAPIView):
    serializer_class = ActionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Action.objects.all()


class ActionCreateView(CreateAPIView):
    serializer_class = ActionSerializer
    permission_classes = (AdminAccess,)
    queryset = Action.objects.all()


class ActionEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = ActionSerializer
    permission_classes = (AdminAccess,)
    queryset = Action.objects.all()


