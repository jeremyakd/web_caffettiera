from django.shortcuts import render
from .models import Service
from .consulta import return_data_from_database

def services(request):
    # ORM
    services = Service.objects.all()
    return render(request, "services/services.html", {'services':services})

def consulta(request):
    return render(request, "services/consulta.html", {'columnas':return_data_from_database})
