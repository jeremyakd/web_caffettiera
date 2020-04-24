from django.contrib import admin
from .models import Link

class LinkAdmin(admin.ModelAdmin):
# Agregamos cfg mas extendida todavia para bloquear el key de nuestras redes ya que lo usamos como clave para acceder a ellas

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Administrador").exists():
            return ('key', 'name')
        else:
            return ('created', 'updated')

admin.site.register(Link, LinkAdmin)