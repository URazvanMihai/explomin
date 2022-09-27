

from django.shortcuts import render, redirect

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

# Create your views here.


def index(request):
  template = loader.get_template('login.html')
  context = {
  }
  return HttpResponse(template.render(context, request))


def loginverification(request):
    user = User.objects.create_user('a', 'lennon@thebeatles.com', 'b')
    user.last_name = 'Lennon'
    user.save()
    return HttpResponse()

@csrf_protect  
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('meniu')
        else:
            messages.success(request, ("Error Logging In"))
            return redirect('login')    

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
        return redirect('login')
