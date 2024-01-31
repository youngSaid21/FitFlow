from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Membre

def index(request, membre_id):
	context = {
		'membre': get_object_or_404(Membre, pk = membre_id),
	}
	return render(request, "FitFlow/index.html", context)

def home(request):
	context = {}
	return render(request, "FitFlow/home.html", context)

def contact(request):
	context = {}
	return render(request, "FitFlow/contact_us.html", context)

def planning(request):
	context = {}
	return render(request, "FitFlow/planning.html", context)
