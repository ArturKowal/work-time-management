from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.api.serializer import PersonSerializer 
from log.models import Log

from django.contrib.auth import get_user_model
User = get_user_model()

@api_view(['GET']) 
def api_detail_who_view(request,id):
	try: person = User.objects.get(id=id)
	except: return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method=="GET":
		try: what=Log.objects.filter(who=id).order_by('when_in').reverse()[0].what
		except: what=False
		serializer = PersonSerializer(person)
		a=serializer.data
		a['what'] = what
		return Response({'person': [a]})
