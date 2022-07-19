from . import views
from django.urls import path



urlpatterns = [
    
    path("", views.index, name="login"),
    path("buttonA", views.login_user),
    path("signin", views.login_user, name="signin")

]