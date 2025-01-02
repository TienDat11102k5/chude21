from django.contrib import admin
from .models import Guest

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_id', 'user_id', 'address', 'city', 'state', 'postal_code', 'name', 'email')
    search_fields = ('address', 'city', 'state', 'postal_code', 'name', 'email')
