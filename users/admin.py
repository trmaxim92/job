from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_employer', 'is_worker', 'is_staff')
    list_filter = ('is_employer', 'is_worker', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'address', 'about', 'profile_picture')}),
        ('Статусы', {'fields': ('is_employer', 'is_worker', 'is_active', 'is_staff', 'is_superuser')}),
        ('Рейтинг', {'fields': ('rating',)}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_employer', 'is_worker'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)