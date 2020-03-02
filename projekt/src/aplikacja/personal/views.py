from django.shortcuts import render, redirect
from log.models import Log
from django.contrib.auth import login
from django.contrib.auth import get_user_model
import datetime


def home_screen_view(request):
	User = get_user_model()
	if request.user.is_authenticated:
		user_id = request.user.id
		month=0
		now = datetime.datetime.now()
		year =  now.year
		if request.method == 'POST':
			month = request.POST.get('field', None)
			user_id = request.POST.get('chuser', None)
			year = request.POST.get('year', None)
			try: user_id = int(user_id)
			except: user_id = request.user.id
			try: month=int(month)
			except: month=0
			try: year=int(year)
			except: year=now.year
		else: month=0

		if month>=1 and month<=12:
			log_in = Log.objects.filter(when_in__month=month,who__id=user_id,what=True,when_in__year=year).order_by('when_in')
			log_out = Log.objects.filter(when_in__month=month,who__id=user_id,what=False,when_in__year=year).order_by('when_in')
		else:
			log_in = Log.objects.filter(who__id=user_id,what=True,when_in__year=year).order_by('when_in')
			log_out = Log.objects.filter(who__id=user_id,what=False,when_in__year=year).order_by('when_in')

		stake= User.objects.get(id=user_id).stake
		position=User.objects.get(id=user_id).position
		my_list=[] ; total_salary=0
		for i in range(len(log_in)):
			curr_data=log_in[i].when_in.date()
			if int(log_in[i].when_in.minute)<10: person_in=str(int(log_in[i].when_in.hour)+1)+':0'+str(log_in[i].when_in.minute)
			else: person_in=str(int(log_in[i].when_in.hour)+1)+':'+str(log_in[i].when_in.minute)

			try:
				#ustalamy person_out
				if int(log_out[i].when_in.minute)<10: person_out=str(int(log_out[i].when_in.hour)+1)+':0'+str(log_out[i].when_in.minute)
				else: person_out=str(int(log_out[i].when_in.hour)+1)+':'+str(log_out[i].when_in.minute)
				b=log_out[i].when_in
				a=log_in[i].when_in
				how_much_time=b-a
				if int(how_much_time.days)>0: days=int(how_much_time.days)
				else: days =0
				hour=int(how_much_time.seconds//3600)
				minutes=int((how_much_time.seconds//60)%60)
				salary = hour*stake + (minutes/60)*stake + days*stake*24

				if hour<10: hour='0'+str(hour)
				else:  hour=str(hour)
				if minutes<10: minutes='0'+str(minutes)
				else:  minutes=str(minutes)
				if days>1: how_much_time = str(days) + ' days ' + hour  +':'+ minutes
				elif days == 1: how_much_time = str(days) + ' day ' + hour  +':'+ minutes
				else: how_much_time = hour  +':'+ minutes

				salary=round(salary,2)
				total_salary+=salary
				my_list.append([curr_data,person_in,person_out,how_much_time,salary])

			except: 
				person_out='-----'
				how_much_time='-----'
				salary ='-----'
				my_list.append([curr_data,person_in,person_out,how_much_time,salary])


		#months=['Styczeń','Luty','Marzec','Kwiecień','Maj','Czerwiec','Lipiec','Sierpień','Wrzesień','Październik','Listopad','Grudzień']

		total_salary=round(total_salary)
		u = User.objects.all()
		personality = User.objects.get(id=user_id)
		context= {'data': my_list,
		'total_salary':total_salary,
		'Users':u,
		'name': personality,
		'year': year,
		}

		return render(request, 'home.html',context)


	if not request.user.is_authenticated:
		return redirect("login")



#from django.contrib.auth import get_user_model
#User = get_user_model()
#u = User.objects.all()
# u = User.objects.get(ident=1234)
# u = User.objects.all()
