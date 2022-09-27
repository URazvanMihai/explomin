from . import views
from django.urls import path

urlpatterns = [ 
    path("", views.index, name="login"),
    path("buttonA", views.loginverification),
    path("signin", views.login_user, name="signin"),
    path("meniu", views.meniu, name = "meniu"),
    # path("logout", views.logout_view, name="logout")
]