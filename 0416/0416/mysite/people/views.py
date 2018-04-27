from django.shortcuts import render
from django.http import HttpResponse
from .models import Name
from django.shortcuts import render_to_response

# Create your views here.

def index(request):
	name = Name.objects.all()
	return render_to_response('people/menu.html',locals())
