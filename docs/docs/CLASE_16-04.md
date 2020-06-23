#### CLASE 16/04

- Terminamos de mapear los link de las redes sociales.
- En nuestro procesador importamos Link y los asignamos a una lista y la pasamos como un contexto general.

```python
def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx
```

Una vez hecho esto solo nos queda comprobar con un if que la clave valga algo y si vale, la mostramos.

    {% if LINK_TWITTER %}
    <a href="{{LINK_TWITTER}}" class="link">
        <span class="fa-stack fa-lg">
        <i class="fa fa-circle fa-stack-2x"></i>
        <i class="fa fa-twitter fa-stack-1x fa-inverse"></i>
        </span>
    </a>
    {% endif %}
    {% if LINK_FACEBOOK %}
    <a href="{{LINK_FACEBOOK}}" class="link">
        <span class="fa-stack fa-lg">
        <i class="fa fa-circle fa-stack-2x"></i>
        <i class="fa fa-facebook fa-stack-1x fa-inverse"></i>
        </span>
    </a>
    {% endif %}
    {% if LINK_INSTAGRAM %}
    <a href="{{LINK_INSTAGRAM}}" class="link">
        <span class="fa-stack fa-lg">
        <i class="fa fa-circle fa-stack-2x"></i>
        <i class="fa fa-instagram fa-stack-1x fa-inverse"></i>
        </span>
    </a>
    {% endif %}

- Creamos nuestra app para genstionar las paginas de la web
    ./manage.py startapp pages
- Creamos su modelo.
```python
from django.db.models import Model, CharField, TextField, DateTimeField, SmallIntegerField

class Page(Model):
    title = CharField(verbose_name="Título", max_length=200)
    content = TextField(verbose_name='Contenido')
    ordering = SmallIntegerField(verbose_name='Orden', default=0)
    created = DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['ordering','title']

    def __str__(self):
        return self.title
```
>Notese que importamos las clases a mano y las usamos en los campos directamente

- Creamos cfg extendida en el admin.py

- Luego migramos y probamos
    python manage.py makemigrations pages
    python manage.py migrate pages

- Creamos las 3 paginas de prueba

- Definimos nuestras vistas
```python
from django.shortcuts import render, get_object_or_404
from .models import Page

def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/sample.html', {'page':page})
```

- Creamos el archivo urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('<int:page_id>/', views.page, name="page"),
]
```
- En el urls.py global incluimos nuestras URLs
```python
path('page/', include('pages.urls')),
```
