from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from rest_framework import permissions


class LeaderAccess(LoginRequiredMixin,permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated and (request.user.role == 'Leader' or request.user.role == 'Admin'):
            return True
        return False


class AdminAccess(LoginRequiredMixin,permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'Admin' or request.user.is_superuser:
            return True
        return False

# class AdminAccess(LoginRequiredMixin):
#     permission_denied_message = "Доступ запрещен!"
#     raise_exception = False
#
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return super().dispatch(request, *args, **kwargs)
#         if not request.user.is_superuser and not request.user.role == 'Admin':
#             return self.handle_no_permission()
#         return super().dispatch(request, *args, **kwargs)


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


# class LeaderAccess(LoginRequiredMixin):
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return super().dispatch(request, *args, **kwargs)
#         if not  request.user.role == 'Leader':
#             return self.handle_no_permission()
#         return super().dispatch(request, *args, **kwargs)
