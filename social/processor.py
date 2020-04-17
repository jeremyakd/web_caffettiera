from .models import Link

def contexto_propio(request):
    context = {}
    for link in Link.objects.all():
        context[link.key] = link.url

    return context