from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .permissions import AdminAccess
from .models import *
# Create your views here.


class IndexUserView(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return reverse_lazy('user:index_admin')
        elif self.request.user.type == 'Employee':
            print('Yes')
            return reverse_lazy('user:index_admin')
        else:
            print('Yest')


class IndexAdmin(AdminAccess,LoginRequiredMixin,generic.TemplateView):
    template_name = 'admin/index.html'


class LeadersView(AdminAccess,LoginRequiredMixin,generic.ListView):
    model = User
    queryset = User.objects.all()
    template_name = 'admin/moderator/list.html'

    def get_context_data(self, **kwargs):
        response = super(LeadersView, self).get_context_data()
        response['roles'] = User.USER_TYPE
        return response


class LeadersCreateView(AdminAccess,LoginRequiredMixin,generic.CreateView):
    model = User
