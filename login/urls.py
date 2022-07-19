from . import views
from django.urls import path



urlpatterns = [
    
    path("", views.login, name="login"),
    path("buttonA", views.login_user),
    # path("signin", views.login_user)

]