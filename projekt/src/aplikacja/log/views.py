from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Log


class LogView(APIView):
    def get(self, request):
        logs = Log.objects.all()
        return Response({"logs": logs})
