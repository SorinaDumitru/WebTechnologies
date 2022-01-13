from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'first_name', 'last_name', 'cnp', 'phone_number')
    ordering = ('-registered_date',)
    list_filter = ('is_doctor', 'is_active', 'is_staff')
    list_display = ('email', 'first_name', 'last_name',
                    'is_doctor', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'registered_date')}),
        ('Personal', {'fields': ('birthday', 'cnp', 'address',)}),
        ('Permissions', {'fields': ('is_doctor', 'is_staff', 'is_active',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name')}),
        ('Personal', {'fields': ('birthday', 'cnp', 'address',)}),
        ('Permissions', {'fields': ('is_doctor', 'is_staff', 'is_active',)}),
    )

    readonly_fields = ["registered_date"]


admin.site.register(NewUser, UserAdminConfig)
