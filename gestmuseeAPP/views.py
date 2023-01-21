from django.shortcuts import render
import random
from django.shortcuts import redirect, render
#pre-built form utilities libraries
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
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



# Create your views here.
def home(request):
	return render(request,'home.html')

def oeuvres(request):
	return render(request,'oeuvres.html')

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


		print(type_abonnee," ",type_abonnement)

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

		user = auth.authenticate(username=email,password=password) 
		
		if user is not None:
			auth.login(request,user)	
			return redirect('home')
		else :
			messages.error(request,"Password missmatchs")
			return redirect('Signinup')
	else: 
		return render(request, 'Signinup.html')
