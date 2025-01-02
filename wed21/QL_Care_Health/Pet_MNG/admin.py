from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('pet_id', 'name', 'species', 'age', 'medical_history', 'customer_id')
    search_fields = ('name', 'species')
