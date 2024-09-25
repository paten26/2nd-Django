from django.contrib import admin
from users.models import Users
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
class UserAdmin(BaseUserAdmin):
    # Pastikan penamaan "fieldsets" benar
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', )}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            },
        ),
    )

    list_display = ('email', 'name', 'is_staff', 'last_login',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'name')  # Field yang sesuai untuk pencarian
    ordering = ('email',)  # Tambahkan urutan untuk tampilan daftar


# Mendaftarkan model `Users` dengan custom `UserAdmin`
admin.site.register(Users, UserAdmin)
