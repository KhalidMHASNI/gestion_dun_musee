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
]