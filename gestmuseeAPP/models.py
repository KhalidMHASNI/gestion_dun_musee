from distutils.command.upload import upload
from email.policy import default
from enum import auto
from math import fabs
import uuid
import random
# User model 
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
#Schedular


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


class Artiste(models.Model):
    nom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    date_deces = models.DateField(blank=True, null=True)
    nationalite = models.CharField(max_length=255)


class Oeuvre(models.Model):
    titre = models.CharField(max_length=255)
    artist = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    type_ouevre = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    type_assurence = models.CharField(max_length=255)

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
    image = models.ImageField(upload_to='gestmuseeAPP\static\img\manifestation')
    notes = models.TextField(blank=True, null=True)

class Conference(models.Model):
    titre = models.CharField(max_length=100)
    theme = models.CharField(max_length=50,blank=True, null=True)
    Conferencier = models.CharField(max_length=100)
    date_debut = models.DateField()
    duree = models.IntegerField(u'Durée de la conférence', help_text=u'Durée en minutes')
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gestmuseeAPP\static\img\conference')
    notes = models.TextField(blank=True, null=True)

class Personel(models.Model):
    nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

    def check_availability(self, date):
        schedule = Schedule.objects.filter(personel=self, date=date)
        if schedule.exists():
            return False
        return True


class Schedule(models.Model):
    personel = models.ForeignKey(Personel, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()

'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='img')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
'''