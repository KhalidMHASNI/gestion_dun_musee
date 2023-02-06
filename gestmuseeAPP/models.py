from datetime import timedelta, timezone,datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime
from django.db import connection


class Abonnee(models.Model):
    prenom = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    type_abonnement = models.CharField(max_length=255)
    type_abonnee = models.CharField(max_length=255)
    date_start = models.DateField()
    date_end = models.DateField()
    numero_credit_carte = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='gestmuseeAPP\static\img\data\profile') 

    @classmethod
    def get_info(self, email, password):
        try:
            abonnee = Abonnee.objects.get(email=email, password=password)
            return [abonnee.prenom, abonnee.nom, abonnee.email, abonnee.type_abonnement, abonnee.type_abonnee, abonnee.date_start, abonnee.numero_credit_carte, abonnee.password, abonnee.image]
        except Abonnee.DoesNotExist:
            return None
    def check_password(self, password):
        return password == self.password


class Artiste(models.Model):
    nom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    date_deces = models.DateField(blank=True, null=True)
    nationalite = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gestmuseeAPP\static\img\data/artiste')


class Oeuvre(models.Model):
    titre = models.CharField(max_length=255)
    artist = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    type_ouevre = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='gestmuseeAPP\static\img\data\oeuvre')
    type_assurence = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

class Salle(models.Model):
    nom = models.CharField(max_length=50)
    capacite = models.IntegerField()
    est_valable = models.BooleanField()

class Manifestation(models.Model):
    titre = models.CharField(max_length=100)
    theme = models.CharField(max_length=50,blank=True, null=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gestmuseeAPP\static\img\data\manifestation')
    notes = models.TextField(blank=True, null=True)

class Conference(models.Model):
    titre = models.CharField(max_length=100)
    theme = models.CharField(max_length=50,blank=True, null=True)
    Conferencier = models.CharField(max_length=100)
    date_debut = models.DateField()
    duree = models.IntegerField(u'Durée de la conférence', help_text=u'Durée en minutes')
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gestmuseeAPP\static\img\data\conference')
    notes = models.TextField(blank=True, null=True)

class Personel(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

    def check_availability(self, date):
        with connection.cursor() as cursor:
            cursor.execute("SELECT personel_id FROM public.\"gestmuseeAPP_schedule\" where date = '%s';" % date)
            perso_data = cursor.fetchall()
            if perso_data:
                return [personel[0] for personel in perso_data]
            return []



class Schedule(models.Model):
    personel = models.ForeignKey(Personel, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.CharField(max_length=12)


class CalendrierMusee(models.Model):
    date = models.DateField()
    reason = models.CharField(max_length=255, null=True, blank=True)
    type_of_reservation = models.CharField(max_length=255, null=True, blank=True)

    @classmethod
    def next_two_weeks_dates(cls):
        two_weeks_from_now = datetime.now() + timedelta(weeks=2)
        dates = cls.objects.filter(date__range=[datetime.now(), two_weeks_from_now]).values_list('date', flat=True)
        return dates



class Reservation(models.Model):
    abonnee = models.ForeignKey(Abonnee, on_delete=models.CASCADE)
    date = models.DateField()
    type_of_reservation = models.CharField(max_length=255)
    personel = models.ForeignKey(Personel, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.type_of_reservation == 'Guided':
            personel = Personel.objects.filter(available=True).first()
            if not personel:
                raise ValidationError("No available personel found for this date.")
            else:
                personel.available = False
                personel.save()
                self.personel = personel
        super().save(*args, **kwargs)
        
    def is_guided(self):
        return self.type_of_reservation == 'Guided'



