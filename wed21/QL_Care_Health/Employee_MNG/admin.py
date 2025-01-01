from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'user_id', 'specialization')
    search_fields = ('specialization',)

# admin.site.register(Employee, EmployeeAdmin) # Bạn có thể sử dụng cách này nếu không dùng decorator
