from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin


class AdminAccess(LoginRequiredMixin):
    permission_denied_message = "Доступ запрещен!"
    raise_exception = False

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
