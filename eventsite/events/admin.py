from django.contrib import admin
from .models import Event, Partner, Video, News

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'start_time', 'end_time', 'location', 'location_details')
    list_filter = ('date',)
    search_fields = ('title', 'location', 'location_details')
    fieldsets = (
        (None, {
            'fields': ('title', 'date', 'start_time', 'end_time', 'description', 'location', 'address', 'location_details', 'image')
        }),
    )

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')
    list_filter = ('publication_date',)
    search_fields = ('title', 'short_description')
    fieldsets = (
        (None, {
            'fields': ('title', 'short_description', 'full_description', 'image')
        }),
    )
    exclude = ('publication_date',)  # Исключаем поле publication_date из формы