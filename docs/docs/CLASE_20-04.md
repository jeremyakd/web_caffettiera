#### CLASE 20/04

- Fusionamos el front y back
- Creamos template tags personalizados
- Creamos un directorio llamado template tags dentro de la app donde queremos añadir esta funcionalidad.
    En nuestro caso pages/templatetags.

- Dentro añadimos un init.py, esto indicará a Python que se trata de un package, 
- Crearemos un script para almacenar nuestros template tags, yo siguiendo el ejemplo oficial de la documentación le voy a llamar pages_extras.py.

    >*__pages_extras.py__*

```python
from django import template
from pages.models import Page

register = template.Library()

@register.simple_tag
def get_pages_list():
    pages = Page.objects.all()
    return pages
```

- Usamos funciones decoradoras por primera vez para registrar nuestro tag.

```django
    {% load pages_extras %}
    {% get_page_list %}
```
- Cargamos ahora si las páginas.
- Le damos un toque más interesante a los enlaces de las páginas, pasando el título en forma de slug.

```django
{% load pages_extras %}
{% get_page_list as page_list %}
{% for page in page_list %}
    <a href="{% url 'page' page.id page.title|slugify %}" class="link">
        {{page.title}}</a> {% if not forloop.last %}·{% endif %} 
{% endfor %}
```
- Modificamos el urls.py 
```python
path('<int:page_id>/<slug:page_slug>/', views.page, name="page"),
```
```python
from django.shortcuts import render, get_object_or_404
from .models import Page

def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/sample.html', {'page': page})
```

- El resultado es interesante y puede mejorar el SEO de las páginas.

- Agregamos un filtro al modelo de páginas
```python
    ordering = SmallIntegerField(verbose_name='Orden', default=0)
```
- En la clase meta . . . 

```python
    ordering = ['ordering','title']
```

- De vuelta a nuestro panel de administrador podemos establecer un número de orden a cada página, un orden que sin cambiar nada se respetará en el frontend.

- Sólo le tenemos que decir al cliente, que si quiere cambiar el orden debe poner un número y que los más pequeños se muestran antes.