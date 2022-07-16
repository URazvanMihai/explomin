from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("/admin1", views.admin, name="admin")

]