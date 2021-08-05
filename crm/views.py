from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .permissions import AdminAccess, AccountantAccess, EmployeeAccess
from .models import *


class IndexUserView(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return reverse_lazy('user:index_admin')
        elif self.request.user.role == 'Admin':
            return reverse_lazy('user:index_admin')
        elif self.request.user.role == 'Accountant':
            return reverse_lazy('user:index_admin')
        elif self.request.user.role == 'Employee':
            return reverse_lazy('user:index_employee')
        elif self.request.user.role == 'Leader':
            return reverse_lazy('user:leader_index')


class IndexAdmin(AdminAccess,LoginRequiredMixin, generic.TemplateView):
    template_name = 'admin/index.html'

    def get_context_data(self, **kwargs):
        response = super(IndexAdmin,self).get_context_data()
        date = datetime.today().strftime('%Y-%m-%d')
        time = datetime.today().strftime('%H:%M')
        response['date'] = date
        response['time'] = time

        today = datetime.today().strftime('%Y-%m-%d')
        user = User.objects.get(id=self.request.user.id)
        try:
            attendance = Attendance.objects.get(user=user,date=today)
            response['attendance'] = attendance
        except:
            pass
        return response


class LeadersView(AdminAccess,LoginRequiredMixin, generic.ListView):
    model = User
    queryset = User.objects.all().filter(role='Leader')
    template_name = 'admin/leader/list.html'

    def get_context_data(self, **kwargs):
        response = super(LeadersView, self).get_context_data()
        roles = []
        date = datetime.today().strftime('%Y-%m-%d')
        time = datetime.today().strftime('%H:%M')
        response['date'] = date
        response['time'] = time
        try:
            for i in User.USER_TYPE:
                roles.append(i[0])
                response['roles'] = roles
            return response
        except:
            return response


class UserDetailedView(AdminAccess,LoginRequiredMixin,generic.DetailView):
    model = User
    template_name = 'admin/leader/detail.html'

    def get_queryset(self):
        queryset = {}
        try:
            queryset = User.objects.all()
            return queryset
        except:
            return queryset

    def get_context_data(self, **kwargs):
        response = super(UserDetailedView, self).get_context_data()
        id = self.kwargs['pk']
        date = datetime.today().strftime('%Y-%m-%d')
        time = datetime.today().strftime('%H:%M')
        response['date'] = date
        response['time'] = time
        user = User.objects.get(id=id)
        try:
            salary = Salary.objects.get(user=user)
            response['salary'] = salary
        except:
            pass
        try:
            balance = Balance.objects.get(user=user)
            response['balance'] = balance
        except:
            pass
        return response


class AccountantView(AdminAccess,generic.ListView):
    model = User
    queryset = User.objects.all().filter(role='Accountant')
    template_name = 'admin/accountant/list.html'

    def get_context_data(self, **kwargs):
        response = super(AccountantView, self).get_context_data()
        roles = []
        date = datetime.today().strftime('%Y-%m-%d')
        time = datetime.today().strftime('%H:%M')
        response['date'] = date
        response['time'] = time
        try:
            for i in User.USER_TYPE:
                roles.append(i[1])
                response['roles'] = roles
            return response
        except:
            return response


class EmployeeListView(AdminAccess,generic.ListView):
    model = User
    queryset = User.objects.all().filter(role='Employee')
    template_name = 'admin/employee/list.html'

    def get_context_data(self, **kwargs):
        response = super(EmployeeListView, self).get_context_data()
        roles = []
        date = datetime.today().strftime('%Y-%m-%d')
        time = datetime.today().strftime('%H:%M')
        response['date'] = date
        response['time'] = time
        try:
            for i in User.USER_TYPE:
                roles.append(i[1])
                response['roles'] = roles
            return response
        except:
            return response


class IndexEmployeeView(EmployeeAccess, generic.ListView):
    template_name = 'employee/index.html'
    context_object_name = 'attendance'

    def get_queryset(self):
        month = datetime.today().strftime('%m')
        queryset = {}
        try:
            queryset = Attendance.objects.all().filter(user=self.request.user,month=month).order_by('-date')
            return queryset
        except:
            return queryset

    def get_context_data(self,**kwargs):
        response = super(IndexEmployeeView, self).get_context_data()
        try:
            status = Attendance.objects.all().filter(user=self.request.user)
            for i in status:
                status = i.status
                finished = i.finished
            response['status'] = status
            response['finished'] = finished
            month = datetime.today().strftime('%B')
            response['month'] = month
            balance = Balance.objects.all().filter(user=self.request.user)
            response['balance'] = balance
            return response
        except:
            return response


class EmployeeAttendanceView(generic.ListView):
    template_name = 'employee/attendance/index.html'
    context_object_name = 'attendance'

    def get_queryset(self):
        queryset = ''
        try:
            queryset = Attendance.objects.all().filter(user=self.request.user).order_by('-date')
            return queryset
        except:
            return queryset


class EmployeeSalaryView(generic.ListView):
    template_name = 'employee/salary/index.html'
    context_object_name = 'salary'

    def get_queryset(self):
        queryset = ''
        try:
            queryset = Salary.objects.all().filter(user=self.request.user)
            print(queryset)
            return queryset
        except:
            print(queryset)
            return queryset


class LeaderIndexView(generic.TemplateView):
    template_name = 'leader/index.html'


class LeaderEmployeeListView(generic.ListView):
    template_name = 'leader/employee/index.html'
    queryset = User.objects.all().filter(role='Employee')