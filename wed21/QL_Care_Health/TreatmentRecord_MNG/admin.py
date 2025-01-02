from django.contrib import admin
from .models import TreatmentRecord

@admin.register(TreatmentRecord)
class TreatmentRecordAdmin(admin.ModelAdmin):
    list_display = ('record_id', 'pet_id', 'veterinarian_id', 'diagnosis', 'prescriptions', 'notes')
    search_fields = ('diagnosis',)
