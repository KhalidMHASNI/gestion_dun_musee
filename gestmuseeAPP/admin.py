from django.contrib import admin
from .models import Abonnee, Oeuvre, Artiste, Salle, Conference, Personel, Schedule, Manifestation
import datetime
import calendar
from django.urls import reverse
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe

# Register your models here.

admin.site.register(Manifestation)
admin.site.register(Artiste)
admin.site.register(Oeuvre)
admin.site.register(Salle)
admin.site.register(Personel)
admin.site.register(Schedule)
admin.site.register(Conference)
admin.site.register(Abonnee)