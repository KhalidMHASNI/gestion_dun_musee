from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import random
from django.shortcuts import redirect, render
# pre-built form utilities libraries
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User,auth

from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User, auth

from .models import *
from django.db import connection
# importing get_template from loader
from django.template.loader import get_template
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import json
from .models import Oeuvre

from .forms import ReservationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


def calendar(request):
    return render(request, 'calendrier.html')

# Create your views here.


def home(request):
    oeuvre = Oeuvre.objects
    conf = Conference.objects.all().order_by('-id')[:1]
    manif = Manifestation.objects.all().order_by('-id')[:2]

    # Get the salle names for each conference
    conf_salle_names = []
    for conference in conf:
        salle = Salle.objects.get(id=conference.salle_id)
        conf_salle_names.append(salle.nom)

    context = {
        'conf': conf,
        'conf_salle_names': conf_salle_names,
        'manif': manif,
        'oeuvre': oeuvre,
    }
    return render(request, 'home.html', context)


def oeuvres(request):
    oeuvre = Oeuvre.objects
    return render(request, 'oeuvres.html', {'oeuvre': oeuvre})


def calendrier(request):
    return render(request, 'calendar.html')


# Signup  page
def SigninupPage(request):
    if request.method == 'POST' and 'btnform2' in request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        num_carte = request.POST['num_carte']
        email = request.POST['email']
        type_abonnement = request.POST['type_abon']
        type_abonnee = request.POST['type']
        password1 = request.POST['password']
        password2 = request.POST['cpassword']

        if password1 == password2:
            if Abonnee.objects.filter(email=email).exists():
                messages.warning(request, 'Email taken')
                return redirect('Signinup')
            else:
                if type_abonnement == "Trimestriel":
                    myuser = User.objects.create_user(
                        username=email, email=email, first_name=first_name, last_name=last_name, password=password1)
                    myuser.save()
                    abonnee = Abonnee.objects.create(id=myuser.id, prenom=first_name, nom=last_name, email=email, type_abonnement=type_abonnement, type_abonnee=type_abonnee,
                                                     numero_credit_carte=num_carte, date_start=datetime.now(), date_end=datetime.now() + relativedelta(months=+3), password=password1)
                    abonnee.save()
                    messages.success(request, "Votre compte est crée .")
                    return redirect('Signinup')
                elif type_abonnement == "Annuel":
                    myuser = User.objects.create_user(
                        username=email, email=email, first_name=first_name, last_name=last_name, password=password1)
                    myuser.save()
                    abonnee = Abonnee.objects.create(id=myuser.id, prenom=first_name, nom=last_name, email=email, type_abonnement=type_abonnement, type_abonnee=type_abonnee,
                                                     numero_credit_carte=num_carte, date_start=datetime.now(), date_end=datetime.now() + relativedelta(years=1), password=password1)
                    abonnee.save()
                    messages.success(request, "Votre compte est crée .")
                    return redirect('Signinup')
                else:
                    myuser = User.objects.create_user(
                        username=email, email=email, first_name=first_name, last_name=last_name, password=password1)
                    myuser.save()
                    abonnee = Abonnee.objects.create(id=myuser.id, prenom=first_name, nom=last_name, email=email, type_abonnement=type_abonnement, type_abonnee=type_abonnee,
                                                     numero_credit_carte=num_carte, date_start=datetime.now(), date_end=datetime.now() + relativedelta(months=+1), password=password1)
                    abonnee.save()
                    messages.success(request, "Votre compte est crée .")
                    return redirect('Signinup')
        else:
            messages.info(request, 'password not matching')
            return redirect('Signinup')

    if request.method == 'POST' and 'btnform1' in request.POST:
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('panel')
        else:
            messages.error(request, "Password missmatchs")
            return redirect('Signinup')
    else:
        return render(request, 'Signinup.html')


def some_view(request):
    with connection.cursor() as cursor:

        cursor.execute("SELECT id, prenom, nom, email, type_abonnement, type_abonnee, date_start, date_end, numero_credit_carte, password, image, last_login FROM public.\"gestmuseeAPP_abonnee\" where id = 2;")
        abonnee_data = cursor.fetchone()
        x = abonnee_data[10]
        abonnee_data = abonnee_data[:10] + (str(x).replace(
            'gestmuseeAPP/static/', ''),) + abonnee_data[11:]
        # print("aduzhduzh ",abonnee_data[10])
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
        cursor.execute("SELECT id, prenom, nom, email, type_abonnement, type_abonnee, date_start, date_end, numero_credit_carte, password, image, last_login FROM public.\"gestmuseeAPP_abonnee\" where id = %s;", [
                       request.user.id])
        abonnee_data = cursor.fetchone()
        x = abonnee_data[10]
        abonnee_data = abonnee_data[:10] + (str(x).replace(
            'gestmuseeAPP/static/', ''),) + abonnee_data[11:]
        y = abonnee_data[7] - abonnee_data[6]
        abonnee_data = list(abonnee_data)
        abonnee_data.append(y.days)
        abonnee_data = tuple(abonnee_data)
        # print("aduzhduzh ",abonnee_data[10])
    unavailable_dates = CalendrierMusee.next_two_weeks_dates()
    formatted_dates = []
    for date in unavailable_dates:
        formatted_date = date.strftime("%Y-%m-%d")
        formatted_dates.append(formatted_date)

    print(formatted_dates)
    oeuvre = Oeuvre.objects
    context = {
        'oeuvre': oeuvre,
        'abonnee_data': abonnee_data,
        'formatted_dates': json.dumps(formatted_dates)
    }

    return render(request, 'panel.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')


def reserver(request):
    if request.method == 'POST':
        abonnee = Abonnee.objects.get(email=request.user.email)

        selected_option = request.POST.get('radio')
        if selected_option == 'non_guide':
            guided = False
        else:
            guided = True

        reservation_date_str = request.POST.get('datepicker')

        reservation_date = datetime.strptime(reservation_date_str, '%m/%d/%Y')

        day_name = reservation_date.strftime("%A")
        available_personnel = []
        for personnel in Personel.objects.all():
            print("TEEST : ", personnel.check_availability(day_name))
            if personnel.check_availability(day_name):
                # print()
                available_personnel.append(personnel)

        print("abonnee: ", abonnee.email)
        print("guided: ", guided)
        print("day_name: ", day_name, "available_personnel: ", available_personnel)

        Reservation.objects.create(
             abonnee=abonnee,
             personel=personnel,
             date=reservation_date,
             type_of_reservation=guided
        )

        messages.success(
            request, "Your reservation has been successfully created.")
        return redirect('panel')
    else:
        return render(request, 'panel.html')


def evenement(request):
    conf = Conference.objects.all()
    manif = Manifestation.objects.all()

    # Get the salle names for each conference
    conf_salle_names = []
    for conference in conf:
        salle = Salle.objects.get(id=conference.salle_id)
        conf_salle_names.append(salle.nom)
        print(conf_salle_names[0])

    manif_salle_names = []
    for manifestation in manif:
        salle = Salle.objects.get(id=manifestation.salle_id)
        manif_salle_names.append(salle.nom)
        print(manif_salle_names[0])

    context = {
        'conf': conf,
        'conf_salle_names': conf_salle_names,
        'manif': manif,
        'manif_salle_names': manif_salle_names,
    }

    return render(request, 'evenement.html', context)


def evt(request):
    return redirect('home')


def sedesabonner(request):
    # Get the Abonnee instance to delete
    abonnee = Abonnee.objects.get(email=request.user.email)
    user = User.objects.get(username=request.user.email)

    # Delete the Abonnee instance
    abonnee.delete()
    user.delete()
    # Redirect the user to a success page
    return redirect('home')


def modify_name_abonnee(request):
    if request.method == 'POST':
        old_nom = request.POST.get('old_nom')
        new_nom = request.POST.get('new_nom')
        old_prenom = request.POST.get('old_prenom')
        new_prenom = request.POST.get('new_prenom')

        abonnee = Abonnee.objects.get(nom=old_nom, prenom=old_prenom)
        abonnee.nom = new_nom
        abonnee.prenom = new_prenom
        abonnee.save()

        return redirect('panel')

    return render(request, 'panel.html')


def modify_passwd_abonnee(request):
    if request.method == 'POST':
        old_pass = request.POST.get('old_pass')
        new_pass = request.POST.get('new_pass')
        com_new_pass = request.POST.get('com_new_pass')
        if (new_pass == old_pass):
            abonnee = Abonnee.objects.get(password=old_pass)
            abonnee.password = new_pass
            abonnee.save()
        else:
            print("Error")

        return redirect('panel')

    return render(request, 'panel.html')


def modify_image_abonnee(request):
    if request.method == 'POST':
        new_image = request.FILES.get('new_image')
        if new_image:
            fs = FileSystemStorage(
                location='C:\\Users\kmhas\Documents\GitHub\gestion_dun_musee\gestmuseeAPP\static\img\data\profile')
            filename = fs.save(new_image.name, new_image)
            uploaded_file_url = fs.url(filename)

            abonnee = request.user
            abonnee.image = uploaded_file_url
            abonnee.save()

            return redirect('panel')

    return render(request, 'panel.html')
