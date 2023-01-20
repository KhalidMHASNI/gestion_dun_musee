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



class Abonnee(models.Model):
    prenom = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    type_abonnement = models.CharField(max_length=255)
    date_start = models.DateField()
    date_end = models.DateField()
    numero_credit_carte = models.CharField(max_length=20)
    cni = models.CharField(max_length=20)
    password = models.CharField(max_length=255) 


class Artist(models.Model):
    nom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    date_deces = models.DateField(blank=True, null=True)
    nationalite = models.CharField(max_length=255)


class Oeuvre(models.Model):
    titre = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    type_ouevre = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    type_assurence = models.CharField(max_length=255)


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