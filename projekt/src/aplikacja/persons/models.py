from django.db import models

class Person(models.Model):
	first_name=  models.CharField(verbose_name="Imie ",max_length=20)
	last_name=   models.CharField(verbose_name="Nazwisko ",max_length=30)
	position=    models.CharField(verbose_name="Stanowisko ",max_length=40)
	e_mail=      models.EmailField(verbose_name="E-mail ",blank=True)
	stake=       models.FloatField(verbose_name="Stawka ",blank=True)#default=12
	own_passwd=	 models.IntegerField(verbose_name="Kod użytkownika ",blank=False)
#
	def __str__(self):
		return self.first_name + ' ' + self.last_name
	class Meta:
		verbose_name="Osoba"
		verbose_name_plural="Osoby"