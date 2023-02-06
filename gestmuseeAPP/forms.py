from datetime import datetime, timedelta,date
from django.utils import timezone
from django import forms
from gestmuseeAPP.models import CalendrierMusee, Reservation, Schedule
import pytz

class ScheduleForm(forms.ModelForm):
    DAYS_OF_WEEK = (
        ('Monday', 'Lundi'),
        ('Tuesday', 'Mardi'),
        ('Wednesday', 'Mercredi'),
        ('Thursday', 'Jeudi'),
        ('Friday', 'Vendredi'),
        #('Saturday', 'Samedi'),
        ('Sunday', 'Dimanche'),
    )

    day = forms.ChoiceField(choices=DAYS_OF_WEEK)

    class Meta:
        model = Schedule
        fields = ['personel', 'start_time', 'end_time', 'day']

    def clean_day(self):
        day = self.cleaned_data['day']
        return day

    def save(self, commit=True):
        schedule = super().save(commit=False)
        day = self.cleaned_data['day']


        schedule.date = day

        if commit:
            schedule.save()

        return schedule

class ReservationForm(forms.ModelForm):
    
    class Meta:
        model = Reservation
        fields = ['abonnee', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        two_weeks_from_now = datetime.now() + timedelta(weeks=2)
        self.fields['date'].widget = forms.SelectDateWidget()
        self.fields['date'].queryset = CalendrierMusee.objects.exclude(date__range=[date.today(), two_weeks_from_now])
