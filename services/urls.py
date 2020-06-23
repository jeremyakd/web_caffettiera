from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name="services"),
    path('consulta/', views.consulta, name="consulta"),
]