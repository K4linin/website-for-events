from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'start_time', 'end_time', 'location', 'location_details')  # Добавляем новое поле в список
    list_filter = ('date',)
    search_fields = ('title', 'location', 'location_details')
    fieldsets = (
        (None, {
            'fields': ('title', 'date', 'start_time', 'end_time', 'description', 'location', 'address', 'location_details', 'image')
        }),
    )