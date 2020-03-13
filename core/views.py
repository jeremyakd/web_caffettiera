from django.shortcuts import HttpResponse
""" 
Inicio home/
Historia about/
Servicios services/
Visítanos store/
Contacto contact/
Blog blog/
Sample sample/ (esta es para páginas de prueba) 
"""
def home(request):
    return HttpResponse('Inicio')

def about(request):
    return HttpResponse('Historia')

def services(request):
    return HttpResponse('Servicios')

def store(request):
    return HttpResponse('Visítanos')

def contact(request):
    return HttpResponse('Contacto')

def blog(request):
    return HttpResponse('Blog')

def sample(request):
    return HttpResponse('Sample')
