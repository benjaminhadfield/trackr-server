"""
A Bill represents a recurring charge that should be paid by one or more parties.
"""

from django.db import models

from utils.model.mixins import TimeStampedModel, PublicIdModel


class Bill(TimeStampedModel, PublicIdModel):
    value = models.PositiveIntegerField()
    message = models.TextField(blank=True)

    def __str__(self):
        return 'Bill {}'.format(self.created)
