from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'location', 'date', 'end_date', 'max_attendees', 'fee')
    list_filter = ('date', 'location', 'owner')
    readonly_fields = ('event_entry_date',)  # Mark the field as read-only in the admin interface
    search_fields = ('title', 'owner__username', 'location')
    date_hierarchy = 'date'
    ordering = ('date',)

    fieldsets = (
        (None, {
            'fields': ('title', 'owner', 'location', 'date','end_date', 'image', 'fee', 'topics', 'food', 'max_attendees')
        }),
    )

# Registering the Event model if not using the decorator
# admin.site.register(Event, EventAdmin)
