"""
A Charge represents a single, one-off amount of money that should be split
across multiple parties.
"""

from datetime import date

from django.db import models

from apps.utils.model.mixins import TimeStampedModel, PublicIdModel


class Charge(TimeStampedModel, PublicIdModel):
    PERIOD_CHOICES = (
        (0, 'once'),
        (1, 'daily'),
        (2, 'monthly'),
        (3, 'weekly'),
        (4, 'bi-weekly'),
        (5, 'yearly'),
    )

    # Detail fields.
    value = models.PositiveIntegerField()  # Amount in pence.
    charge_date = models.DateField(default=date.today)  # Date to send charge.
    is_paid = models.BooleanField(default=False)
    # Meta fields.
    title = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)
    # Repeating charge fields.
    period = models.PositiveSmallIntegerField(default=0, choices=PERIOD_CHOICES)
    end_date = models.DateField(blank=True, null=True)

    def is_active(self):
        today = date.today()
        return (self.charge_date < today) and (self.end_date > today)

    def __str__(self):
        return 'Charge {}'.format(self.created)
