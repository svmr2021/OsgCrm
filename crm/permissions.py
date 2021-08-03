from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin


class AdminAccess(LoginRequiredMixin):
    permission_denied_message = "Доступ запрещен!"
    raise_exception = False

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        if not request.user.is_superuser and not request.user.role == 'Admin':
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AccountantAccess(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        if not  request.user.role == 'Accountant':
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class EmployeeAccess(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        if not  request.user.role == 'Employee':
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
