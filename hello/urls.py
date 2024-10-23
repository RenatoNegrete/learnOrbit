from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("login_continue/", views.loginContinue, name="loginContinue"),
    path('redirect/', views.redirect_view, name='redirect_view'),
    path("home/", views.home, name="home"),
    path("perfil/", views.perfil, name="perfil"),
    path("info_curso", views.info_curso, name="info_curso")
]