from rest_framework.generics import * 
from rest_framework.permissions import *
from Api.v1.crm.serializers import *
from crm.models import *


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()


class UserEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
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
    serializer_class = AttendanceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Attendance.objects.all()

    # def post(self, request, *args, **kwargs):
    #     today = datetime.today().strftime('%Y-%m-%d')
    #     id = request.data['user']
    #     user = User.objects.get(id=id)
    #     try:
    #         obj = Attendance.objects.get(user=user, data=today)
    #         obj.time_out = datetime.now().strftime('%H:%M')
    #         obj.save()
    #     except:
    #         obj = Attendance(user=user)
    #         obj.save()
    #     return super(AttendanceCreateView, self).post(request)


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


class QuestionsListView(ListAPIView):
    serializer_class = QuestionsSerializer
    permission_classes = (AllowAny,)
    queryset = Questions.objects.all()


class QuestionsCreateView(CreateAPIView):
    serializer_class = QuestionsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Questions.objects.all()


class QuestionsEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Questions.objects.all()


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


