from django.db import models
from django.conf import settings

class Log(models.Model):
	CHOICES = (
    (True, 'Wchodze'),
    (False, 'Wychodze')
	)
	who=    models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Kto ')
	what = models.BooleanField(verbose_name='Akcja ',choices=CHOICES,default=True)
	when_in=   models.DateTimeField(verbose_name='Kiedy', auto_now_add=True)
	class Meta:
		verbose_name="Log "
		verbose_name_plural="Logi "