from django.db import models
from django.contrib.auth import get_user_model

class Event(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # Assuming owner is a user
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    end_date = models.DateTimeField()  # End date of the event
    event_entry_date = models.DateTimeField(auto_now_add=True)  # Automatically sets on creation
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)  # Requires Pillow
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    topics = models.TextField()  # You could use a ManyToManyField if topics are a separate model
    food = models.TextField(blank=True, null=True)
    max_attendees = models.PositiveIntegerField(default=0, help_text="Maximum number of attendees the user can organize for events.")

    def __str__(self):
        return self.title
