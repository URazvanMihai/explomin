from . import views
from django.urls import path


app_name = "administrator"

urlpatterns = [
    path("", views.index, name="index"),
    path("user" , views.user, name="user"),
    path("pontaj", views.create_post , name="pontaj"),
    path("login", views.loginpage, name = "login"),
    path("buttonA", views.loginverification),
    path("signin", views.login_user, name="signin"),
    path("meniu", views.meniu, name = "meniu"),
    path("logout", views.logout_view, name="logout"),
    path("delete_pontaj/<int:id>", views.delete_pontaj, name="delete_pontaj"),
    path("enable_edit_pontaj", views.enable_edit_pontaj, name="enable_edit_pontaj"),
]
