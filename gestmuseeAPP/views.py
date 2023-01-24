from django.shortcuts import render
import random
from django.shortcuts import redirect, render
#pre-built form utilities libraries
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User,auth

from django.contrib import messages
from django.http import JsonResponse

from .models import Abonnee
from .models import *
import io
from django.http import FileResponse

from django.http import HttpResponse
from django.views.generic import View
 
#importing get_template from loader
from django.template.loader import get_template
from datetime import date, datetime,timedelta
from dateutil.relativedelta import relativedelta
import json

from .forms import ReservationForm
from django.contrib.auth import login,authenticate


# Create your views here.
def home(request):
	return render(request,'home.html')

def oeuvres(request):
	return render(request,'oeuvres.html')

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
					abonnee = Abonnee.objects.create(prenom=first_name, nom=last_name, email=email, type_abonnement=type_abonnement,type_abonnee=type_abonnee,numero_credit_carte=num_carte, date_start=datetime.now(), date_end=datetime.now() + relativedelta(months=+3), password=password1)
					abonnee.save()
					messages.success(request, "Votre compte est crée .")
					return redirect('Signinup')
				elif type_abonnement == "Annuel":
					abonnee = Abonnee.objects.create(prenom=first_name, nom=last_name, email=email, type_abonnement=type_abonnement,type_abonnee=type_abonnee,numero_credit_carte=num_carte, date_start=datetime.now(), date_end=datetime.now() + relativedelta(years=1), password=password1)
					abonnee.save()
					messages.success(request, "Votre compte est crée .")
					return redirect('Signinup')
				else :
					abonnee = Abonnee.objects.create(prenom=first_name, nom=last_name, email=email, type_abonnement=type_abonnement,type_abonnee=type_abonnee,numero_credit_carte=num_carte, date_start=datetime.now(), date_end=datetime.now() + relativedelta(months=+1), password=password1)
					abonnee.save()
					messages.success(request, "Votre compte est crée .")
					return redirect('Signinup')
		else:
			messages.info(request,'password not matching')
			return redirect('Signinup')


	if request.method== 'POST' and 'btnform1' in request.POST:
			email = request.POST['email']
			password = request.POST['password']
			abonnee_info = Abonnee.get_info(email, password)
			user = authenticate(request, email=email, password=password)
			if user:
				if user.check_password(password):
					login(request,user)
					return render(request, 'login.html', {'user': request.user})
				else:
					return render(request, 'Signinup', {'error': 'Invalid credentials'})
			else:
				return render(request, 'Signinup', {'error': 'Invalid credentials'})

	else: 
		return render(request, 'Signinup.html')


def some_view(request):
	unavailable_dates = CalendrierMusee.next_two_weeks_dates()
	formatted_dates = []
	for date in unavailable_dates:
		formatted_date = date.strftime("%Y-%m-%d")
		formatted_dates.append(formatted_date)
	context1 = {'formatted_dates': json.dumps(formatted_dates)}
	#print(context)
	return render(request, 'make_reservation.html', context1)

def login(request):
	if request.user.is_authenticated:
		return render(request,'login',{'user': request.user})
	else:
		print("errrrrrrror")

def panel(request):
    if 'abonnee_id' in request.session:
        abonnee = Abonnee.objects.get(id=request.session['abonnee_id'])
        return render(request, 'panel.html', {'abonnee': abonnee})
    else:
        return redirect('login')

def logout(request):
    if 'abonnee_id' in request.session:
        del request.session['abonnee_id']
    return redirect('login')
