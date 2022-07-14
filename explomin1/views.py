
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

from explomin1.models import People

# Create your views here.

def index(request):
  peoples = People.objects.all().values()
  template = loader.get_template('explomin1/index.html')
  context = {
    'peoples': peoples,
  }
  return HttpResponse(template.render(context, request))
  
# def add(request):
#   template = loader.get_template('add.html')
#   return HttpResponse(template.render({}, request))