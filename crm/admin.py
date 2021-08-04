from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = User
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Main", {
            "fields": (
                "first_name",
                "last_name",
                'middle_name',
                'img',
                'file',
                "email",
                "phone",
                'home_phone',
                'birth_place',
                "birth_date",
                "role",
                'is_superuser',
                'is_active',
                'is_staff',
            )
        }),
    )


admin.site.register(User,CustomUserAdmin)
admin.site.register(Attendance)
admin.site.register(Time)
admin.site.register(Salary)
admin.site.register(Balance)
admin.site.register(SendSalary)
admin.site.register(StandUp)
admin.site.register(Question)

