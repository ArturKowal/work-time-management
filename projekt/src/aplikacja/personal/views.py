from django.shortcuts import render
from account.models import Account
from django.shortcuts import render
from log.models import Log


def home_screen_view(request):
	
	context = {}
	logowania = Log.objects.all()
	context['logowania'] = logowania

	return render(request, "home.html", context)



