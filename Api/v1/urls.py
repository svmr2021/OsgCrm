from django.urls import path, include

urlpatterns = [path('crm/', include('Api.v1.crm.urls'))]
from django.urls import path, include


urlpatterns += [path('crm/',include('Api.v1.crm.urls'))]
