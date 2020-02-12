from django.shortcuts import render
from account.models import Account


def home_screen_view(request):
	
	context = {}
	accounts = Account.objects.all()
	context['accounts'] = accounts

	return render(request, "home.html", context)

	# Search
#	query = ""
#	if request.GET:
#		query = request.GET.get('q', '')
#		context['query'] = str(query)