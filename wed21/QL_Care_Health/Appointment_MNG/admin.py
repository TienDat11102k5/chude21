from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'customer_id', 'pet_id', 'veterinarian_id', 'date', 'time', 'status', 'notes')
    search_fields = ('date', 'status')
