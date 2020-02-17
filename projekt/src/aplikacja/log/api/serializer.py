from rest_framework import serializers
from log.models import Log
from django.contrib.auth import get_user_model
User = get_user_model()


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['who','what']


#from django.contrib.auth import get_user_model
# User = get_user_model()
# u = User.objects.get(ident=1234)
# u = User.objects.all()