from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from log.models import Log
from log.api.serializer import LogSerializer

from django.contrib.auth import get_user_model
User = get_user_model()

@api_view(['POST']) 
def api_create_log_view(request):
	u = User.objects.get(ident=2222)
	logs = Log(who=u)
	if request.method=="POST":
		my_data=request.data.copy()
		ids=request.data.__getitem__('who')
		try: what=Log.objects.filter(who=ids).order_by('when_in').reverse()[0].what
		except: what=False
		if what == False: what=True
		else: what=False
		my_data.__setitem__('what', what )
		serializer = LogSerializer(logs, data=my_data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.data,serializer.errors, status=status.HTTP_400_BAD_REQUEST)

