from django.contrib import admin
from .models import Veterinarian

@admin.register(Veterinarian)
class VeterinarianAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'user_id', 'specialization')
    search_fields = ('specialization',)
