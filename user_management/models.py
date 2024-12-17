from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now  # Import for timezone-aware datetime
from django.db import models

class CustomUser(AbstractUser):
    # Remove the user_type field, keeping it minimal
    phone_number = models.CharField(max_length=15, blank=True, null=True, help_text="Contact phone number")
    address = models.TextField(blank=True, null=True, help_text="Customer's address")
    is_vegetarian = models.BooleanField(default=False, help_text="Is the user vegetarian?")
    birthday = models.DateField(blank=True, null=True, help_text="User's birthday")
    last_tobacco = models.DateField(blank=True, null=True, help_text="User's birthday")
    is_smoker = models.BooleanField(default=False, help_text="Is the user a smoker?")

    def days_since_last_tobacco(self):
        """Calculate the number of days since last tobacco use."""
        if self.last_tobacco:
            return (now().date() - self.last_tobacco).days
        return None  # Return None if last_tobacco is not set

    def __str__(self):
        return self.username
