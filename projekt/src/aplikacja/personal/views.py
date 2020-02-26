from django.shortcuts import render
from account.models import Account
from django.shortcuts import render, redirect
from log.models import Log
from django.contrib.auth import login
from django.contrib.auth import get_user_model


def home_screen_view(request):
	if request.user.is_authenticated:
		user_id = request.user.id
		if request.method == 'POST':
			month = request.POST.get('field', None)
			user_id = request.POST.get('chuser', None)
			try:
				user_id = int(user_id)
			except:
				user_id = request.user.id
			try:
				month=int(month)
			except: month=13 
		else: month=13 ; start_date=2 ; end_date=2 ; user_id = request.user.id

		User = get_user_model()
		personality = User.objects.get(id=user_id)
		#>>> s='2020-02-14'
		#>>> who=Log.objects.filter(when_in__lte=s,when_in__gte='2020-02-13',who__id=2)

		if month == 1: start_date = '2020-01-01' ; end_date = '2020-01-31'
		elif month == 2: start_date = '2020-02-01' ; end_date = '2020-02-29'
		elif month == 3: start_date = '2020-03-01' ; end_date = '2020-03-31'
		elif month == 4: start_date = '2020-04-01' ; end_date = '2020-04-30'
		elif month == 5: start_date = '2020-05-01' ; end_date = '2020-05-31'
		elif month == 6: start_date = '2020-06-01' ; end_date = '2020-06-30'
		elif month == 7: start_date = '2020-07-01' ; end_date = '2020-07-31'
		elif month == 8: start_date = '2020-08-01' ; end_date = '2020-08-31'
		elif month == 9: start_date = '2020-09-01' ; end_date = '2020-09-30'
		elif month == 10: start_date = '2020-10-01' ; end_date = '2020-10-31'
		elif month == 11: start_date = '2020-11-01' ; end_date = '2020-11-30'
		elif month == 12: start_date = '2020-12-01' ; end_date = '2020-12-31'

		if month>=1 and month<=12:
			log_in = Log.objects.filter(when_in__lte=end_date,when_in__gte=start_date,who__id=user_id,what=True).order_by('when_in')
			log_out = Log.objects.filter(when_in__lte=end_date,when_in__gte=start_date,who__id=user_id,what=False).order_by('when_in')
		else:
			log_in = Log.objects.filter(who__id=user_id,what=True).order_by('when_in')
			log_out = Log.objects.filter(who__id=user_id,what=False).order_by('when_in')



		stake=request.user.stake
		position=request.user.position
		my_list=[]
		total_salary=0
		#log_in = Log.objects.filter(who__id=request.user.id,what=True).order_by('when_in')
		#log_out = Log.objects.filter(who__id=request.user.id,what=False).order_by('when_in')
		if len(log_in)==len(log_out):
			for i in range(len(log_in)):
				curr_data=str(log_in[i].when_in)[0:10]
				person_in=str(log_in[i].when_in)[10:16] ### naprawić + 1 h
				person_out=str(log_out[i].when_in)[10:16] ### naprawić + 1 h
				person_in_hour=person_in[1:3]
				#print("łoooolluju",person_in_hour)
				person_in = person_in[3:]
				person_out_hour=person_out[1:3]
				person_out = person_out[3:]
			#	if person_in_hour>="00" and person_in_hour>="22": 
			#		person_in=str(int(person_in_hour)+1)+person_in
				#elif person_in_hour=="23": 
				#	person_in='00'+person_in

				if '22'>=person_in_hour>="00": person_in=str(int(person_in_hour)+1)+person_in
				elif person_in_hour=="23": person_in='00'+person_in


				if '22'>=person_out_hour>="00": person_out=str(int(person_out_hour)+1)+person_out
				elif person_out_hour=="23": person_out='00'+person_out

				a=log_in[i].when_in ; b=log_out[i].when_in
				how_much_time=b-a
				how_much=str(how_much_time)[0:5]
				if how_much[-1]==':': how_much_time=str(how_much_time)[0:4]
				else: how_much_time=str(how_much_time)[0:5]
				try:
					hour=int(how_much_time[:2])
					minutes=int(how_much_time[3:])
				except:
					hour=int(how_much_time[:1])
					minutes=int(how_much_time[2:])
				salary=hour*stake+(minutes/60)*stake
				salary=round(salary,2)
				total_salary=total_salary+salary

				my_list.append([curr_data,person_in,person_out,how_much_time,salary])
		total_salary=round(total_salary)
		User = get_user_model()
		u = User.objects.all()
		context= {'data': my_list,
		'total_salary':total_salary,
		'Users':u,
		'name': personality,
		}

		return render(request, 'home.html',context)


	if not request.user.is_authenticated:
		return redirect("login")








	#context = {}
	#logowania = Log.objects.all()
	#context['logowania'] = logowania
	#return render(request, "home.html", context)

	#from django.contrib.auth import get_user_model
#User = get_user_model()
#u = User.objects.all()
# u = User.objects.get(ident=1234)
# u = User.objects.all()


#Choices are: id, what, when_in, who, who_id




	# if request.user.is_authenticated:
	# 	logowania = Log.objects.filter(who__id=request.user.id)
	# 	context= {'logowania': logowania}
	# 	return render(request, 'home.html',context)


# {% for Log in logowania %}
# <tr>
# <td>{{ Log.who }}</td>
# <td>{{ Log.what }}</td>
# <td>{{ Log.when_in }}</td>
# </tr>
# {% endfor %}
# </table>