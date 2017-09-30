"""
A Charge represents a single, one-off amount of money that should be split
across multiple parties.
"""

from django.db import models

from utils.model.mixins import TimeStampedModel, PublicIdModel


class Charge(TimeStampedModel, PublicIdModel):
    value = models.PositiveIntegerField()
    message = models.TextField(blank=True)

    def __str__(self):
        return 'Charge {}'.format(self.created)
