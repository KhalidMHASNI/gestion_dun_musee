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

    path('make_reservation/', views.make_reservation, name='make_reservation')
]