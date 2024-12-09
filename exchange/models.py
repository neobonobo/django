from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models import Sum

class ExchangeItem(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=50, help_text="Unit of the item, e.g., kg, pieces, liters")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.unit})"


class Exchange(models.Model):
    giver = models.ForeignKey(get_user_model(), related_name="exchanges_given", on_delete=models.CASCADE)
    receiver = models.ForeignKey(get_user_model(), related_name="exchanges_received", on_delete=models.CASCADE)
    item = models.ForeignKey(ExchangeItem, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    value_estimate = models.DecimalField(max_digits=10, decimal_places=2, help_text="Estimated value of this exchange in currency")
    timestamp = models.DateTimeField(default=timezone.now)
    is_settled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.giver} gave {self.quantity} {self.item} to {self.receiver} on {self.timestamp.date()} - Settled: {self.is_settled}"


class Settlement(models.Model):
    user1 = models.ForeignKey(get_user_model(), related_name="settlements_initiated", on_delete=models.CASCADE)
    user2 = models.ForeignKey(get_user_model(), related_name="settlements_received", on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    settled_on = models.DateTimeField(blank=True, null=True)

    def calculate_balance(self):
        # Total value given by user1 to user2
        total_given_by_user1 = Exchange.objects.filter(
            giver=self.user1, receiver=self.user2, is_settled=False
        ).aggregate(total=Sum('value_estimate'))['total'] or 0
        
        # Total value given by user2 to user1
        total_given_by_user2 = Exchange.objects.filter(
            giver=self.user2, receiver=self.user1, is_settled=False
        ).aggregate(total=Sum('value_estimate'))['total'] or 0

        # Calculate net balance
        self.amount_due = total_given_by_user1 - total_given_by_user2
        self.save()

    def settle_exchanges(self):
        # Mark all unsettled exchanges between user1 and user2 as settled
        Exchange.objects.filter(
            giver=self.user1, receiver=self.user2, is_settled=False
        ).update(is_settled=True)
        Exchange.objects.filter(
            giver=self.user2, receiver=self.user1, is_settled=False
        ).update(is_settled=True)

        # Mark settlement as finalized
        self.settled_on = timezone.now()
        self.amount_due = 0
        self.save()

    def __str__(self):
        return f"Settlement between {self.user1} and {self.user2} - Due: {self.amount_due}"
