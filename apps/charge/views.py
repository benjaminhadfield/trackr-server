from django.db.models import Q

from rest_framework import viewsets

from .models import Charge
from .serializers import ChargeSerializer


class ChargeViewSet(viewsets.ModelViewSet):
    serializer_class = ChargeSerializer

    def get_queryset(self):
        # Return all charges that the user is a member of.
        return Charge.objects.filter(
            Q(created_by=self.request.user) |
            Q(split_with__in=[self.request.user])
        )

