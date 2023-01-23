from datetime import datetime, timedelta
from django.utils import timezone
from django import forms
from gestmuseeAPP.models import CalendrierMusee, Reservation, Schedule

class ScheduleForm(forms.ModelForm):
    DAYS_OF_WEEK = (
        ('Lundi', 'Lundi'),
        ('Mardi', 'Mardi'),
        ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'),
        ('Vendredi', 'Vendredi'),
        #('Samedi', 'Samedi'),
        ('Dimanche', 'Dimanche'),
    )

    day = forms.ChoiceField(choices=DAYS_OF_WEEK)

    class Meta:
        model = Schedule
        fields = ['personel', 'start_time', 'end_time', 'day']

    def clean_day(self):
        day = self.cleaned_data['day']
        date = datetime.datetime.now().date()
        while date.strftime("%A") != day:
            date += datetime.timedelta(days=1)
        return date

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['abonnee', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        now = timezone.now()
        two_weeks_from_now = now + timedelta(weeks=2)
        available_dates = CalendrierMusee.objects.filter(date__range=[now, two_weeks_from_now], type_of_reservation='available')
        print(date__range=[now, two_weeks_from_now])
        self.fields['date'].queryset = available_dates
