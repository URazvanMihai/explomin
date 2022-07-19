
from django.shortcuts import render, redirect

from django.template import loader
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.


def login(request):
  template = loader.get_template('login.html')
  context = {
  }
  return HttpResponse(template.render(context, request))


# def loginverification(request):
#     # # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#     # user.last_name = 'Lennon'
#     # user.save()
   
   

#     return HttpResponse() 


# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
#         ...      

def login_user(request):
    if request.metod == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('administrator.html')
        else:
            # messages.success(request), ("Error Logging in")
            return redirect('login.html')    


    else: render(request, 'login.html')


