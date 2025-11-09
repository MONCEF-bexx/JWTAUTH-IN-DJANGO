from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from .models import Student , Teacher , User

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'role', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),  
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )
