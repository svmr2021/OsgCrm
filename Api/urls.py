from django.urls import path, include


urlpatterns = [path('v1/', include('Api.v1.urls'))]
