from datetime import date

from django.db import models
from django.contrib.auth.models import User


class StandingOrder(models.Model):
    PERIOD_CHOICES = (
        (0, 'daily'),
        (1, 'weekly'),
        (2, 'bi-weekly'),
        (3, 'monthly'),
        (4, 'yearly'),
    )

    title = models.CharField(max_length=255)
    value = models.PositiveIntegerField()
    period = models.PositiveSmallIntegerField(default=3, choices=PERIOD_CHOICES)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(blank=True, null=True)
    split_with = models.ManyToManyField(User)

    def is_active(self):
        today = date.today()
        after_or_on_start_date = self.start_date <= today
        before_end_date = not self.end_date or self.end_date > today
        return after_or_on_start_date and before_end_date

    def __str__(self):
        return self.title
