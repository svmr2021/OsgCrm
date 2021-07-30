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
                "email",
                "phone",
                "birth_date",
                "role",
                'is_superuser',
            )
        }),
    )


admin.site.register(User,CustomUserAdmin)