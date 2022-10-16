from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from administrator.models import People, Locations
from .models import Postform
from .forms import Postform



# Create your views here.
def index(request):
  job = ['I','II','III']
  days = ['Luni', 'Marti', 'Miercuri', 'Joi',' Vineri']
  locations = Locations.objects.all().values()
  peoples = People.objects.all().values()
  template = loader.get_template('administrator.html')
  context = {
    'peoples': peoples,
    'locations': locations,
    'days': days,
    'job':job,
  }
  return HttpResponse(template.render(context, request))


def user(request):
  job = ['I','II','III']
  days = ['Luni', 'Marti', 'Miercuri', 'Joi',' Vineri']
  locations = Locations.objects.all().values()
  peoples = People.objects.all().values()
  template = loader.get_template('user.html')
  context = {
    'peoples': peoples,
    'locations': locations,
    'days': days,
    'job':job,
  }
  return HttpResponse(template.render(context, request))



def pontaj(request):
  template = loader.get_template('pontaj.html')
  weekdays = range(1,32)
  context = {
    'weekdays': weekdays,

  }
  return HttpResponse(template.render(context, request)) 



def loginpage(request):
  template = loader.get_template('login.html')
  context = {
  }
  return HttpResponse(template.render(context, request))


# def loginverification(request):
#     user = User.objects.create_user('a', 'lennon@thebeatles.com', 'b')
#     user.last_name = 'Lennon'
#     user.save()
#     return HttpResponse()

def loginverification(request):
    user = User.objects.get(id=1)
    assign_role(user, 'user')
    return HttpResponse()



@csrf_protect  
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('administrator:meniu')
        else:
            messages.success(request, "Error Logging In")
            return redirect('administrator:login')    

    else:
        return render(request, 'signin')


def meniu(request):
    template = loader.get_template('meniu.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def logout_view(request):
    user = request.user
    if user != None:
        logout(request)
        return redirect('administrator:login')


# CRUD

def create_post(request):
  context= {}

  form = Postform(request.POST or None)
  if form.is_valid():
      form.save()


  context['form'] =  form

  return render(request,"pontaj.html",context)    
