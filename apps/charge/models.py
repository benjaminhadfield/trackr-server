"""
A Charge represents a single, one-off amount of money that should be split
across multiple parties.
"""

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

from apps.utils.model.mixins import TimeStampedModel, PublicIdModel
from apps.standing_order.models import StandingOrder


class Charge(TimeStampedModel, PublicIdModel):
    # User that created the charge.
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='charge_requests'
    )
    # Charge amount in pence.
    value = models.PositiveIntegerField()
    # Date to send charge.
    charge_date = models.DateTimeField(default=timezone.now)
    # Boolean denoting whether the charge has been paid.
    is_paid = models.BooleanField(default=False)
    # Relation to the standing order this charge was created from.
    standing_order = models.ForeignKey(
        StandingOrder,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    # Users to split the charge with.
    split_with = models.ManyToManyField(User, related_name='charges')
    # Title of the charge.
    title = models.CharField(max_length=255, blank=True)
    # Any additional details.
    message = models.TextField(blank=True)

    def is_active(self):
        now = timezone.now()
        return self.charge_date <= now

    def mark_as_paid(self):
        self.is_paid = True
        self.save()

    def __str__(self):
        return 'Charge {}'.format(self.created)
