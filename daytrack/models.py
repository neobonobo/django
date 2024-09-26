from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Day(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='days')
    date = models.DateField(default=timezone.now)
    wake_up_time = models.DateTimeField(null=True, blank=True)
    activities = models.TextField(blank=True, null=True)  # Track activities done during the day.

    def __str__(self):
        return f"{self.user.username}'s day on {self.wake_up_time}"
    class Meta:
        unique_together = ('user', 'date')  # Ensure one entry per user per day

