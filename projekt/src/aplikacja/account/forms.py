from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.contrib.auth import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
	email=forms.EmailField(max_length=60, help_text='Wprowadź poprawny adres email')

	class Meta:
		model=Account
		fields=('email','first_name','last_name','ident','password1','password2')

class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = Account
		fields = ('email', 'first_name','last_name','ident' )

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_first_name(self):
		first_name = self.cleaned_data['first_name']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(first_name=first_name)
		except Account.DoesNotExist:
			return first_name
		raise forms.ValidationError('Username "%s" is already in use.' % first_name)

	def clean_last_name(self):
		last_name = self.cleaned_data['last_name']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(last_name=last_name)
		except Account.DoesNotExist:
			return last_name
		raise forms.ValidationError('Username "%s" is already in use.' % last_name)

	def clean_first_name(self):
		ident = self.cleaned_data['ident']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(ident=ident)
		except Account.DoesNotExist:
			return ident
		raise forms.ValidationError('Username "%s" is already in use.' % ident)






