from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['ident','first_name','last_name','id',]