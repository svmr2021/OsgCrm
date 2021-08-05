from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

app_name = 'user'

urlpatterns = [
    path('', IndexUserView.as_view(), name='index'),
    path('admin/', IndexAdmin.as_view(), name='index_admin'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='login.html'), name='logout'),

    path('leaders/', LeadersView.as_view(), name='leaders_list'),
    path('leaders/<int:pk>/', UserDetailedView.as_view(), name='leaders_detail'),

    path('accountant/', AccountantView.as_view(), name='accountant_list'),
    path('accountant/<int:pk>/', UserDetailedView.as_view(), name='leaders_detail'),

    path('employee/', EmployeeListView.as_view(), name='employee_list'),
    path('employee/<int:pk>/', UserDetailedView.as_view(), name='leaders_detail'),

    path('employee_index/', IndexEmployeeView.as_view(), name='index_employee'),
    path('employee_attendance/', EmployeeAttendanceView.as_view(), name='employee_attendance'),
    path('employee_salary/', EmployeeSalaryView.as_view(), name='employee_salary'),

    path('leader_index/', LeaderIndexView.as_view(), name='leader_index'),
    path('base_leader/',LeaderBaseView.as_view(), name = 'leader_base'),
    path('employee_list/', LeaderEmployeeListView.as_view(), name='leader_employee_list'),
    path('employee_detail/<int:pk>/', LeaderEmployeeDetailView.as_view(), name='leader_employee_detail'),
    path('employee_attendance_list/',LeaderEmployeeAttendance.as_view(),name='leader_employee_attendance_list'),
    path('employee_salary_list/', LeaderEmployeeSalaryHistory.as_view(), name='leader_employee_salary_history_list'),
]
