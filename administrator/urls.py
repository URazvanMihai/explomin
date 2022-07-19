from . import views
from django.urls import path


app_name = "administrator"

urlpatterns = [
    path("", views.index, name="index")
]