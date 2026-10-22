from django.urls import path

from . import views

urlpatterns = [
    path("", views.get, name="get"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("home/", views.home_view, name="home"),
    path("profesor/", views.profesor_view, name="profesor"),
]
