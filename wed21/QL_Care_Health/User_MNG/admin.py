from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'fullname', 'birthdate', 'gender', 'phone', 'email', 'role_id')
    search_fields = ('fullname', 'email')
