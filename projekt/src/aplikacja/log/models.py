from django.db import models

from django.db import models

from persons.models import Person

from django.utils.timezone import now

#from django.utils.translation import ugettext_lazy as lazy

class SignIn(models.Model):
	who=    models.ForeignKey(Person, on_delete=models.CASCADE)
#	do_you_in=   models.BooleanField(default=True)
#	do_you_out=   models.BooleanField(default=True)
	when_in=   models.DateTimeField(default=now) 
#	when_out=   models.DateTimeField(blank=True) 
	def __str__(self):
		return self.who.first_name #+ self.when_in
	class Meta:
		verbose_name="Zalogowany"
		verbose_name_plural="Zalogowani"
			

class SignOut(models.Model):
	who=    models.ForeignKey(Person, on_delete=models.CASCADE)
#	do_you_in=   models.BooleanField(default=True)
#	do_you_out=   models.BooleanField(default=True)
	when_out=   models.DateTimeField(default=now) 
#	when_out=   models.DateTimeField(blank=True)
	class Meta:
		verbose_name="Wylogowany"
		verbose_name_plural="Wylogowani"