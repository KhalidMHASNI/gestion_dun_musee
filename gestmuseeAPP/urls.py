from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.urls import include, path


app_name='gestmuseeApp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('Signinup/',views.SigninupPage, name="Signinup"),
    path('oeuvres/',views.oeuvres, name="oeuvres"),
    path('calendar/',views.calendrier, name="calendar"),
    path('panel/',views.panel, name="panel"),
    path('login/', views.login, name='login'),
    path('make_reservation/', views.some_view, name='make_reservation'),
    path('panel/logout',views.logout, name="logout"),
    path('calendrier/',views.calendar, name='calendar'),
    path('panel/reserver',views.reserver, name='reserver'),
    path('evenement/',views.evenement, name='evenement'),
]