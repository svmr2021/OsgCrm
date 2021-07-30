from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

app_name = 'user'

urlpatterns = [
    path('', IndexUserView.as_view(), name='index'),
    path('admin/', IndexAdmin.as_view(), name='index_admin'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login.html'), name='logout'),
    path('leaders/', LeadersView.as_view(), name='leaders_list'),

    path('leaders/<int:pk>/',LeaderDetailedView.as_view(),name='leaders_detail'),
]
