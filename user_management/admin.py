from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Customizing the displayed fields for the user in the admin
    fieldsets = UserAdmin.fieldsets  # Keeps default fields
    add_fieldsets = UserAdmin.add_fieldsets  # Keeps default fields for adding users

    # Including groups (such as Root and Kalee) in the user form
    filter_horizontal = ('groups', 'user_permissions',)

# Register the CustomUser model with the admin
admin.site.register(CustomUser, CustomUserAdmin)

# Register the Group model in case you want to manage groups manually in the admin
admin.site.unregister(Group)  # Optional: To prevent default Django group management
admin.site.register(Group)
