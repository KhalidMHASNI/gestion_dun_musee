from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('Signinup/',views.SigninupPage, name="Signinup"),
    path('oeuvres/',views.oeuvres, name="oeuvres")

]