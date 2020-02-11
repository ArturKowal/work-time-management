from django.db import models

from django.db import models

from django.contrib.auth import settings

from django.utils.timezone import now


class Log(models.Model):
	CHOICES = (
    (True, 'Wchodze'),
    (False, 'Wychodze')
	)
	who=    models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	in_out = models.BooleanField(choices=CHOICES,default=True)

	when_in=   models.DateTimeField(verbose_name='Kiedy ', auto_now_add=True)
#	when_out=   models.DateTimeField(blank=True) 
#	def __str__(self):
#		return self.who.first_name + self.last_name 
	class Meta:
		verbose_name="Log "
		verbose_name_plural="Logi "
			