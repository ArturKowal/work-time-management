from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.api.serializer import PersonSerializer

from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(['GET']) 
def api_detail_who_view(request,ident):
	try:
		person = User.objects.get(ident=ident)
	except Person.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	#logs = Log.objects.all()
	if request.method=="GET":
		serializer = PersonSerializer(person)
		return Response(serializer.data)














