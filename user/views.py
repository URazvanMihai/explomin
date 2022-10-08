
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

from user.models import  People, Locations

# Create your views here.

def index(request):
  job = ['I','II','III']
  days = ['Luni', 'Marti', 'Miercuri', 'Joi',' Vineri']
  locations = Locations.objects.all().values()
  peoples = People.objects.all().values()
  template = loader.get_template('user/index.html')
  context = {
    'peoples': peoples,
    'locations': locations,
    'days': days,
    'job':job,
  }
  return HttpResponse(template.render(context, request))



def pontaj(request):
  template = loader.get_template('pontaj.html')
  context = {

  }
  return HttpResponse(template.render(context, request)) 
