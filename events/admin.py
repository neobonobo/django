from django.contrib import admin
from .models import Event, Attendee

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'location', 'date', 'end_date', 'max_attendees', 'fee')
    list_filter = ('date', 'location', 'owner')
    readonly_fields = ('event_entry_date',)
    search_fields = ('title', 'owner__username', 'location')
    date_hierarchy = 'date'
    ordering = ('date',)

    fieldsets = (
        (None, {
            'fields': ('title', 'owner', 'location', 'date', 'end_date', 'image', 'fee', 'topics', 'food', 'max_attendees')
        }),
    )

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'email', 'phone', 'contribution_type', 'registration_date')
    list_filter = ('event', 'contribution_type', 'registration_date')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('registration_date',)
