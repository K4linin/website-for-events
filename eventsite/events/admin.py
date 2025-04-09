from django.contrib import admin
from .models import Event, Partner, Video, News, Conference, ConferenceEvent, Speaker, ConferencePhoto, ConferenceVideo, EventPhoto, EventVideo, EventActivity

# Inline для фотографий, видео и активностей мероприятия
class EventPhotoInline(admin.TabularInline):
    model = EventPhoto
    extra = 1

class EventVideoInline(admin.TabularInline):
    model = EventVideo
    extra = 1

class EventActivityInline(admin.TabularInline):
    model = EventActivity
    extra = 1

# Блок "Главный сайт"
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
    exclude = ('publication_date',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Блок "Мероприятия"
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'start_time', 'end_time', 'location')
    list_filter = ('date',)
    search_fields = ('title', 'location')
    inlines = [EventActivityInline, EventPhotoInline, EventVideoInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'date', 'start_time', 'end_time', 'description', 'goals', 'location', 'address', 'main_image', 'additional_info', 'latitude', 'longitude')
        }),
    )

@admin.register(EventPhoto)
class EventPhotoAdmin(admin.ModelAdmin):
    list_display = ('event',)
    list_filter = ('event',)
    fieldsets = (
        (None, {
            'fields': ('event', 'image')
        }),
    )

@admin.register(EventVideo)
class EventVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'event')
    list_filter = ('event',)
    search_fields = ('title', 'event__title')
    fieldsets = (
        (None, {
            'fields': ('event', 'title', 'video_file')
        }),
    )

@admin.register(EventActivity)
class EventActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'event', 'start_time', 'end_time', 'location')
    list_filter = ('event',)
    search_fields = ('title', 'event__title')
    fieldsets = (
        (None, {
            'fields': ('event', 'title', 'start_time', 'end_time', 'description', 'location')
        }),
    )

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'start_date', 'end_date', 'organizers', 'format', 'goal_image', 'goal_text', 'plan')
        }),
    )

@admin.register(ConferenceEvent)
class ConferenceEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'conference', 'date', 'start_time', 'end_time')
    list_filter = ('conference', 'date')
    search_fields = ('title', 'conference__title')
    fieldsets = (
        (None, {
            'fields': ('conference', 'title', 'date', 'start_time', 'end_time', 'format', 'online_link')
        }),
    )

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'conference')
    list_filter = ('conference',)
    search_fields = ('name', 'conference__title')
    fieldsets = (
        (None, {
            'fields': ('conference', 'name', 'bio', 'photo')
        }),
    )

@admin.register(ConferencePhoto)
class ConferencePhotoAdmin(admin.ModelAdmin):
    list_display = ('conference',)
    list_filter = ('conference',)
    fieldsets = (
        (None, {
            'fields': ('conference', 'image')
        }),
    )

@admin.register(ConferenceVideo)
class ConferenceVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'conference')
    list_filter = ('conference',)
    search_fields = ('title', 'conference__title')
    fieldsets = (
        (None, {
            'fields': ('conference', 'title', 'video_file')
        }),
    )