from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from account.forms import RegistrationForm

def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email 			= form.cleaned_data.get('email')
			ident 			= form.cleaned_data.get('ident')
			first_name 		= form.cleaned_data.get('first_name')
			last_name 		= form.cleaned_data.get('last_name')
			raw_password 	= form.cleaned_data.get('password1')
			account 		= authenticate(email=email,password=raw_password,first_name=first_name,ident=ident,last_name=last_name)
			login(request,account)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form= RegistrationForm()
		context['registration_form'] = form
	return render(request, 'register.html',context)



