from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .serializers import UserSerializer


class UserViewsets(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @list_route(methods=['GET'])
    def me(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
