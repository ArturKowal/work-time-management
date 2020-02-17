from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm


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



def logout_views(request):
	 logout(request)
	 return redirect('/')

#############################################



def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	return render(request, "login.html", context)


def account_view(request):

	if not request.user.is_authenticated:
			return redirect("login")

	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
					"email": request.POST['email'],
					"first_name": request.POST['first_name'],
					"ident": request.POST['ident'],
					"last_name": request.POST['last_name'],
			}
			form.save()
			context['success_message'] = "Updated"
	else:
		form = AccountUpdateForm(

			initial={
					"email": request.user.email, 
					"first_name": request.user.first_name,
					"ident": request.user.ident,
					"last_name": request.user.last_name,
				}
			)

	context['account_form'] = form

	return render(request, "account.html", context)


def must_authenticate_view(request):
	return render(request, 'must_authenticate.html', {})


