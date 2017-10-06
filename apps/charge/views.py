from django.db.models import Q

from rest_framework import viewsets

from .models import Charge
from .serializers import ChargeSerializer


class ChargeViewSet(viewsets.ModelViewSet):
    serializer_class = ChargeSerializer
    search_fields = ('created_by',)

    def get_queryset(self):
        # Return all charges that the user is a member of.
        return Charge.objects.filter(
            Q(created_by=self.request.user) |
            Q(split_with__in=[self.request.user])
        ).order_by('-charge_date', '-created')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
