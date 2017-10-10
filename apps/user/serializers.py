from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True, source='get_short_name')

    class Meta:
        model = User
        fields = ('id', 'username', 'name')
