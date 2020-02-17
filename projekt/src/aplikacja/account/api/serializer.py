from rest_framework import serializers
#from account.models import Log
from django.contrib.auth import get_user_model
User = get_user_model()


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['ident','first_name','last_name','id']


#from django.contrib.auth import get_user_model
# User = get_user_model()
# u = User.objects.get(ident=1234)
# u = User.objects.all()