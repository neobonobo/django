from django.contrib import admin
from .models import Day

# Customize the admin interface for the Day model
class DayAdmin(admin.ModelAdmin):
    list_display = ('user',  )
    list_filter = ('user',  )
    search_fields = ('user__username', )

# Register the Day model with the custom admin interface
admin.site.register(Day, DayAdmin)
