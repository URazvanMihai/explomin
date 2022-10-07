from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("user/pontaj" , views.pontaj, name="pontaj")
]