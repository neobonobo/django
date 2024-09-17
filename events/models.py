from django.db import models
from django.contrib.auth import get_user_model

class Event(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    end_date = models.DateTimeField()
    event_entry_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional fee for event
    topics = models.TextField()
    food = models.TextField(blank=True, null=True)
    max_attendees = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Attendee(models.Model):
    CONTRIBUTION_CHOICES = [
        ('money', 'Money'),  # Monetary fee
        ('manPower', 'Manpower'),  # Helping or bringing food
    ]
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    contribution_type = models.CharField(max_length=8, choices=CONTRIBUTION_CHOICES, default='money')
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} attending {self.event.title} via {self.contribution_type}"
