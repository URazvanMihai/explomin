
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

from explomin1.models import  People, Locations

# Create your views here.

def index(request):
  job = ['I','II','III']
  days = ['Luni', 'Marti', 'Miercuri', 'Joi',' Vineri']
  locations = Locations.objects.all().values()
  peoples = People.objects.all().values()
  template = loader.get_template('explomin1/index.html')
  context = {
    'peoples': peoples,
    'locations': locations,
    'days': days,
    'job':job,
  }
  return HttpResponse(template.render(context, request))



def administrator(request):
  job = ['I','II','III']
  days = ['Luni', 'Marti', 'Miercuri', 'Joi',' Vineri']
  locations = Locations.objects.all().values()
  peoples = People.objects.all().values()
  peoples = People.objects.all().values()
  template = loader.get_template('explomin1/administrator.html')
  context = {
    'peoples': peoples,
    'locations': locations,
    'days': days,
    'job':job,
  }
  return HttpResponse(template.render(context, request))



 
  
# def add(new_people):
#     people = People.objects.create(name="Alex")
    
#     template = loader.get_template('explomin1/index.html')
#     return HttpResponse(template.render({}, new_people))


    
  


