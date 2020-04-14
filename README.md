## Intro
Vamos a crear una app de una cafeteria.
La idea es practicar lo que vimos y aplicar conceptos nuevos

### CLASE 12/03

- Creamos el proyecto nuevo
  - django-admin startproject web_empresa
- Creamos la app core
  - manage.py startapp core
- Creamos las vistas en el urls.py
  - Inicio home/
  - Historia about/
  - Servicios services/
  - Visítanos store/
  - Contacto contact/
  - Blog blog/
  - Sample sample/ (esta es para páginas de prueba)

### CLASE 21/03

- creamos app blog
- templates
- urls
- settings.py
- models
- admin
- migraciones


### CLASE 24/03

- Campos avanzados del admin (falta ver)
- relaciones MTM
- relaciones OTM
- Filtros


### CLASE 27/03

- Repasamos y reforzamos la clase anterior
- Vimos con profundidad modelos avanzados de admin
- Vimos campos nuevos de filtro
- Grupos de usuario (FALTA)

users:
admin_1
oper_1
pass: root_1111

correlativos nombre pass

## CLASE 30/03

- filtro | linebreaks
- creamos vista categorias
- creamos template categorias
- mapeamos su url con un parametro que recibe en la consulta
- fitro inverso categories.get_posts.all

### Tarea:
- Terminar las categorias, agregarle enlace.

## CLASE 13/04

- terminamos los templates blog y categorias
- repasamos campos propios en el admin
- vimos filtros de fecha
- vimos como cortar URL para machear y poder resaltar la seccion actual
- creamos la app social
- creamos su modelo
- asignamos configuracion avanzada
- creamos un procesador de contexto
- lo importamos y lo probamos