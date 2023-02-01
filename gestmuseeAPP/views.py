from django.shortcuts import render
import random
from django.shortcuts import redirect, render
#pre-built form utilities libraries
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User,auth

from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User,auth

from .models import *
from django.db import connection
#importing get_template from loader
from django.template.loader import get_template
from datetime import date, datetime,timedelta
from dateutil.relativedelta import relativedelta
import json
from .models import Oeuvre

from .forms import ReservationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def calendar(request):
	return render(request,'calendrier.html')

# Create your views here.

def home(request):
	oeuvre = Oeuvre.objects
	return render(request,'home.html',{'oeuvre': oeuvre})

def oeuvres(request):
	oeuvre = Oeuvre.objects
	return render(request,'oeuvres.html',{'oeuvre': oeuvre})

def calendrier(request):
	return render(request,'calendar.html')


#Signup  page
def SigninupPage(request):
	if request.method=='POST' and 'btnform2' in request.POST: 
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		num_carte = request.POST['num_carte']
		email = request.POST['email']
		type_abonnement = request.POST['type_abon']
		type_abonnee = request.POST['type']
		password1 = request.POST['password']
		password2 = request.POST['cpassword']


		if password1 == password2 :
			if Abonnee.objects.filter(email=email).exists():
				messages.warning(request,'Email taken')
				return redirect('Signinup')
			else :
				if type_abonnement== "Trimestriel":
					myuser = User.objects.create_user(username=email, email=email,first_name=first_name,last_name=last_name ,password=password1)
					myuser.save()
					abonnee = Abonnee.objects.create(id=myuser.id,prenom=first_name, nom=last_name, email=email, type_abonnement=type_abonnement,type_abonnee=type_abonnee,numero_credit_carte=num_carte, date_start=datetime.now(), date_end=datetime.now() + relativedelta(months=+3), password=password1)
					abonnee.save()
					messages.success(request, "Votre compte est crée .")
					return redirect('Signinup')
				elif type_abonnement == "Annuel":
					myuser = User.objects.create_user(username=email, email=email,first_name=first_name,last_name=last_name ,password=password1)
					myuser.save()
					abonnee = Abonnee.objects.create(id=myuser.id,prenom=first_name, nom=last_name, email=email, type_abonnement=type_abonnement,type_abonnee=type_abonnee,numero_credit_carte=num_carte, date_start=datetime.now(), date_end=datetime.now() + relativedelta(years=1), password=password1)
					abonnee.save()
					messages.success(request, "Votre compte est crée .")
					return redirect('Signinup')
				else :
					myuser = User.objects.create_user(username=email, email=email,first_name=first_name,last_name=last_name ,password=password1)
					myuser.save()
					abonnee = Abonnee.objects.create(id=myuser.id,prenom=first_name, nom=last_name, email=email, type_abonnement=type_abonnement,type_abonnee=type_abonnee,numero_credit_carte=num_carte, date_start=datetime.now(), date_end=datetime.now() + relativedelta(months=+1), password=password1)
					abonnee.save()
					messages.success(request, "Votre compte est crée .")
					return redirect('Signinup')
		else:
			messages.info(request,'password not matching')
			return redirect('Signinup')


	if request.method== 'POST' and 'btnform1' in request.POST:
		username = request.POST['email']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password) 

		if user is not None:
			auth.login(request,user)
			return redirect('panel')
		else :
			messages.error(request,"Password missmatchs")
			return redirect('Signinup')
	else: 
		return render(request, 'Signinup.html')


def some_view(request):
	with connection.cursor() as cursor:
		
		cursor.execute("SELECT id, prenom, nom, email, type_abonnement, type_abonnee, date_start, date_end, numero_credit_carte, password, image, last_login FROM public.\"gestmuseeAPP_abonnee\" where id = 2;")
		abonnee_data = cursor.fetchone()
		x = abonnee_data[10]
		abonnee_data = abonnee_data[:10] + (str(x).replace('gestmuseeAPP/static/', ''),) + abonnee_data[11:]
		#print("aduzhduzh ",abonnee_data[10])
	unavailable_dates = CalendrierMusee.next_two_weeks_dates()
	formatted_dates = []
	for date in unavailable_dates:
		formatted_date = date.strftime("%Y-%m-%d")
		formatted_dates.append(formatted_date)
	context = {
            'abonnee_data': abonnee_data,
            'formatted_dates': json.dumps(formatted_dates)
        }
	return render(request, 'make_reservation.html', context)

# id = abonnee_data[0]
# prenom = abonnee_data[1]
# nom = abonnee_data[2]
# type_abonnement = abonnee_data[3]

def panel(request):
	# print(request.user.id)
	with connection.cursor() as cursor:
		cursor.execute("SELECT id, prenom, nom, email, type_abonnement, type_abonnee, date_start, date_end, numero_credit_carte, password, image, last_login FROM public.\"gestmuseeAPP_abonnee\" where id = %s;",[request.user.id])
		abonnee_data = cursor.fetchone()
		x = abonnee_data[10]
		abonnee_data = abonnee_data[:10] + (str(x).replace('gestmuseeAPP/static/', ''),) + abonnee_data[11:]
		# print("aduzhduzh ",abonnee_data[10])
	unavailable_dates = CalendrierMusee.next_two_weeks_dates()
	formatted_dates = []
	for date in unavailable_dates:
		formatted_date = date.strftime("%Y-%m-%d")
		formatted_dates.append(formatted_date)
	oeuvre = Oeuvre.objects
	context = {
			'oeuvre': oeuvre,
            'abonnee_data': abonnee_data,
            'formatted_dates': json.dumps(formatted_dates)
        }

	return render(request,'panel.html', context)

def logout(request):
	auth.logout(request)
	return redirect('home')

def reserver(request):
    if request.method == 'POST':
        abonnee = Abonnee.objects.get(email=request.user.email)
        reservation_type = request.POST.get('type')
        reservation_date_str = request.POST.get('datepicker')
		
        reservation_date = datetime.strptime(reservation_date_str, '%d/%m/%Y')

        
        print("abonnee: ", abonnee.email)
        print("reservation_type: ", reservation_type)
        print("reservation_date: ", reservation_date)
		
        Reservation.objects.create(
             abonnee=abonnee, 
             date=reservation_date,
             type_of_reservation=reservation_type
        )
        messages.success(request, "Your reservation has been successfully created.")
        return redirect('panel')
    else:
        return render(request, 'panel.html')
