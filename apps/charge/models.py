"""
A Charge represents a single, one-off amount of money that should be split
across multiple parties.
"""

from datetime import date

from django.db import models
from django.contrib.auth.models import User

from apps.utils.model.mixins import TimeStampedModel, PublicIdModel
from apps.standing_order.models import StandingOrder


class Charge(TimeStampedModel, PublicIdModel):
    # Detail fields.
    value = models.PositiveIntegerField()  # Amount in pence.
    charge_date = models.DateField(default=date.today)  # Date to send charge.
    is_paid = models.BooleanField(default=False)
    standing_order = models.ForeignKey(
        StandingOrder, on_delete=models.CASCADE, null=True, blank=True)
    split_with = models.ManyToManyField(User)
    # Meta fields.
    title = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)

    def is_active(self):
        today = date.today()
        return self.charge_date <= today

    def __str__(self):
        return 'Charge {}'.format(self.created)
