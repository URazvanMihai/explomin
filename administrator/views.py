import json
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from administrator.models import People, Locations, Pontaj, PontajToggleEdit, Masini, Puscari, PuscareMembriiEchipei

# Create your views here.
def index(request):
  job = ['I','II','III']
  days = ['Luni', 'Marti', 'Miercuri', 'Joi', 'Vineri']
  roles = ['Coordonator', 'Artificier', 'Azot']
  locations = Locations.objects.all().values()
  peoples = People.objects.all().values()
  masini = Masini.objects.all().values()
  template = loader.get_template('administrator.html')
  context = {
    'peoples': peoples,
    'locations': locations,
    'days': days,
    'jobs':job,
    'roluri': roles,
    'masini': masini
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
    if request.method == "POST":
        ruta_input = request.POST['ruta']
        km_input = request.POST['km']
        ore_input = request.POST['ore']
        obs_input = request.POST['obs']

        post_form = Pontaj(ruta=ruta_input, km=km_input, ore=ore_input, observatii=obs_input)
        post_form.save()
        return redirect('administrator:pontaj')
    else:
        template = loader.get_template('pontaj.html')
        pontaj_db = Pontaj.objects.all().order_by('created_at')
        pontaj_list = []

        for pontaj in pontaj_db:
            p, created = PontajToggleEdit.objects.get_or_create(pontaj_id=pontaj.id)
            pontaj_obj = {
                'id': pontaj.id,
                'ruta': pontaj.ruta,
                'km': pontaj.km,
                'ore': pontaj.ore,
                'obs': pontaj.observatii,
                'is_edit_mode': p.is_edit_mode,
                'created_at': pontaj.created_at,
                'updated_at': pontaj.updated_at
            }
            pontaj_list.append(pontaj_obj)

        context = {
            'pontaje': pontaj_list
        }
        return HttpResponse(template.render(context, request))

@csrf_protect
def delete_pontaj(request, id):
    if request.method == "POST":
        pontaj = Pontaj.objects.get(id=id)
        pontaj.delete()
        return redirect('administrator:pontaj')

@csrf_protect
def enable_edit_pontaj(request):
    pontaj_edit = PontajToggleEdit.objects.get(pontaj_id=request.POST['pontaj_id'])
    pontaj_edit.is_edit_mode = request.POST['is_edit_mode'] == 'true'
    pontaj_edit.save()
    return redirect('administrator:pontaj')

@csrf_protect
def update_pontaj(request, id):
    if request.method == "POST":
        pontaj = Pontaj.objects.get(id=id)

        if pontaj is None:
            return redirect('administrator:pontaj')
        else:
            pontaj.ruta = request.POST['ruta']
            pontaj.km = request.POST['km']
            pontaj.ore = request.POST['ore']
            pontaj.observatii = request.POST['obs']
            pontaj.save()
            return redirect('administrator:pontaj')

@csrf_protect
def create_puscare(request):
    if request.method == "POST":
        cariera = request.POST['cariera']
        ora = request.POST['ora']
        nume_coordonator = request.POST['nume_coordonator']
        masina_coordonator = request.POST['masina_coordonator']
        nume_artificier = request.POST['nume_artificier']
        masina_artificier = request.POST['masina_artificier']
        nume_azot = request.POST['nume_azot']
        masina_azot = request.POST['masina_azot']
        membrii_echipa = json.loads(request.POST['membrii_echipa'])

        puscare = Puscari(
            cariera=cariera,
            ora=ora,
            nume_coordonator=nume_coordonator,
            masina_coordonator=masina_coordonator,
            nume_artificier=nume_artificier,
            masina_artificier=masina_artificier,
            nume_azot=nume_azot,
            masina_azot=masina_azot,
            membrii_id=None)
        puscare.save()

        for membru in membrii_echipa:
            nume = membru['nume']
            masina = membru['masina']

            membru_model = PuscareMembriiEchipei(puscare_id=puscare.id, nume_membru=nume, masina_membru=masina)
            membru_model.save()

    return HttpResponse('success')

@csrf_protect
def get_puscare_by_date_range(request):
    if request.method == "POST":
        start_date = request.POST['start_date'] 
        end_date = request.POST['end_date']

        puscari_by_date = Puscari.objects.filter(ziua__gte=start_date, ziua__lte=end_date)
        puscari_list = list(puscari_by_date.values())

        return JsonResponse({'data': puscari_list})
    return JsonResponse({'data': 'not implemented'})

