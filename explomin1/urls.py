from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("administrator", views.administrator, name="administrator")

]