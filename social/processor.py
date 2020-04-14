from .models import Link

def contexto_propio(request):
    context = {'prueba': 'Contexto global'}
    return context