from django.contrib import admin
from .models import Abonnee, Oeuvre, Artiste, Salle, Conference, Personel, Schedule, Manifestation,CalendrierMusee,Reservation
import datetime
import calendar
from django.urls import reverse
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe
from .forms import ScheduleForm


class ScheduleInline(admin.TabularInline):
    model = Schedule
    form = ScheduleForm
    extra = 7
    max_num = 7
    
class PersonelAdmin(admin.ModelAdmin):
    inlines = [ScheduleInline]
    list_display = ('nom','prenom')

admin.site.register(Personel, PersonelAdmin)

# Register your models here.

admin.site.register(Manifestation)
admin.site.register(Artiste)
admin.site.register(Oeuvre)
admin.site.register(Salle)
admin.site.register(Schedule)
admin.site.register(Conference)
admin.site.register(Abonnee)
admin.site.register(CalendrierMusee)
admin.site.register(Reservation)
