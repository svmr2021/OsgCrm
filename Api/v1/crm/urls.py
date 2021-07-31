from django.urls import path
from Api.v1.crm.views import *
urlpatterns = [
  path('user/list/',UserListView.as_view()),
  path('user/create/',UserCreateView.as_view()),
  path('user/detail/<int:pk>',UserEditView.as_view())
]
urlpatterns += [
  path('salary/list/',SalaryListView.as_view()),
  path('salary/create/',SalaryCreateView.as_view()),
  path('salary/detail/<int:pk>',SalaryEditView.as_view())
]
urlpatterns += [
  path('attendance/list/',AttendanceListView.as_view()),
  path('attendance/create/',AttendanceCreateView.as_view()),
  path('attendance/detail/<int:pk>',AttendanceEditView.as_view())
]
urlpatterns += [
  path('balance/list/',BalanceListView.as_view()),
  path('balance/create/',BalanceCreateView.as_view()),
  path('balance/detail/<int:pk>',BalanceEditView.as_view())
]
urlpatterns += [
  path('standup/list/',StandUpListView.as_view()),
  path('standup/create/',StandUpCreateView.as_view()),
  path('standup/detail/<int:pk>',StandUpEditView.as_view())
]
urlpatterns += [
  path('question/list/',QuestionListView.as_view()),
  path('question/create/',QuestionCreateView.as_view()),
  path('question/detail/<int:pk>',QuestionEditView.as_view())
]
urlpatterns += [
  path('time/list/',TimeListView.as_view()),
  path('time/create/',TimeCreateView.as_view()),
  path('time/detail/<int:pk>',TimeEditView.as_view())
]
