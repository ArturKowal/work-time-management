from rest_framework import serializers
from log.models import Log
from django.contrib.auth import get_user_model
User = get_user_model()


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['who','what',]