
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

from explomin1.models import  People

# Create your views here.

def index(request):
  peoples = People.objects.all().values()
  template = loader.get_template('explomin1/index.html')
  context = {
    'peoples': peoples,
  }
  return HttpResponse(template.render(context, request))

# def index(request):
#   locations = Locations.objects.all().values()
#   template = loader.get_template('explomin1/index.html')
#   context = {
#     'locations': locations,
#   }
#   return HttpResponse(template.render(context, request))


 
  
# def add(new_people):
#     people = People.objects.create(name="Alex")
    
#     template = loader.get_template('explomin1/index.html')
#     return HttpResponse(template.render({}, new_people))

# def add(new_days):
#   days = new_days.object.create(["Luni","Marti","Miercuri","Joi","Vineri"])
#   template = loader.get_template('explomin1/index.html')
#   return HttpResponse(template.render({}, days))
    
  


