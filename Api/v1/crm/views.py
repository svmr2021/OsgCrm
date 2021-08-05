from rest_framework.generics import *
from rest_framework.permissions import *
from Api.v1.crm.serializers import *
from crm.models import *
from crm.permissions import AdminAccess


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()


class UserEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = (AdminAccess, IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()


class SalaryListView(ListAPIView):
    serializer_class = SalarySerializer
    permission_classes = (AllowAny,)
    queryset = Salary.objects.all()


class SalaryCreateView(CreateAPIView):
    serializer_class = SalarySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Salary.objects.all()


class SalaryEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = SalarySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
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
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Attendance.objects.all()


class BalanceListView(ListAPIView):
    serializer_class = BalanceSerializer
    permission_classes = (AllowAny,)
    queryset = Balance.objects.all()


class BalanceCreateView(CreateAPIView):
    serializer_class = BalanceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Balance.objects.all()


class BalanceEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = BalanceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
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
    permission_classes = (AllowAny,)
    queryset = SendSalary.objects.all()


class SendSalaryCreateView(CreateAPIView):
    serializer_class = SendSalarySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = SendSalary.objects.all()


class SendSalaryEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = SendSalaryEditSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = SendSalary.objects.all()
