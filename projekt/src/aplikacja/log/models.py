from django.db import models

from django.db import models

from django.conf import settings

from django.utils.timezone import now


class Log(models.Model):
	CHOICES = (
    (True, 'Wchodze'),
    (False, 'Wychodze')
	)
	who=    models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Kto ')
	what = models.BooleanField(verbose_name='Akcja ',choices=CHOICES,default=True)
	when_in=   models.DateTimeField(verbose_name='Kiedy')#, auto_now_add=True)
#	when_out=   models.DateTimeField(blank=True) 
#	def __str__(self):
#		return self.who.first_name + self.last_name 
	class Meta:
		verbose_name="Log "
		verbose_name_plural="Logi "
			

# class Dsiplay_log(id):
# 	my_list=[]
# 	who=Log.objects.filter(who__id=id)
# 	for i in range(len(who)):
# 		if who[i].what==True:
# 			when_in=who[i].when_in
# 			if who[i+1]==False:
# 				when_out=who[i+1].when_in
# 				my_list.append([who[i].])




#who=Log.objects.filter(when_in__lte='2020-02-14',when_in__gte='2020-02-13',who__id=2)

#from django.contrib.auth import get_user_model
# User = get_user_model()
# u = User.objects.get(ident=1234)
# u = User.objects.all()


#Choices are: id, what, when_in, who, who_id
