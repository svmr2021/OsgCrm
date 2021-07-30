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
                "email",
                "phone",
                "birth_date",
                "role",
                'is_superuser',
                'is_active',
                'is_staff',
            )
        }),
    )


admin.site.register(User,CustomUserAdmin)