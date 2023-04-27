from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('entrar/', views.entrar, name="entrar"),
    path('chat/<str:nome>/Salas', views.chat, name="chat"),
]