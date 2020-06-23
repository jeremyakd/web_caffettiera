from django.urls import path
from . import views

urlpatterns = [
        path('', views.contact, name="contact"),
        path('respuesta/', views.respuesta, name="respuesta"), #Opcional para redirigir a esta pagina
    ]
