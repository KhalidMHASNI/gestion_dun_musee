from django.shortcuts import render
import random
from django.shortcuts import redirect, render
#pre-built form utilities libraries
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import JsonResponse

from .models import Profile
from .models import *
import io
from django.http import FileResponse

from django.http import HttpResponse
from django.views.generic import View
 
#importing get_template from loader
from django.template.loader import get_template

# Create your views here.
def home(request):
	return render(request,'home.html')