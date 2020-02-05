from django.db import models

class Person(models.Model):
	first_name=  models.CharField(max_length=20)
	last_name=   models.CharField(max_length=30)
	position=    models.CharField(max_length=40)
	e_mail=      models.EmailField(blank=True)
	stake=       models.FloatField(default=12)
	own_passwd=	 models.IntegerField(blank=False)
#
	def __str__(self):
		return self.first_name + ' ' + self.last_name + ', Stanowisko: ' + self.position