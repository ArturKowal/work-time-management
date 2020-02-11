from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account

class RegistrationForm(UserCreationForm):
	email=forms.EmailField(max_length=60, help_text='Wprowadź poprawny adres email')

	class Meta:
		model=Account
		fields=('email','first_name','last_name','ident','password1','password2')