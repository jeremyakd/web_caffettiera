from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')


    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now)
    # El datetime published nos permite establecer una fecha manual de publicación de la entrada, así como la imagen que subiremos al directorio media/blog y es optativa.
    

    content = models.TextField(max_length=200, verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True) # parametros opcionales
    categories = models.ManyToManyField(Category, verbose_name='Categorías', related_name="get_posts")
    # Many2Many apuntando al modelo Category y que nos permitirá seleccionar una o más categorías.

    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    # La relación ForeignKey, haciendo referencia el primer parámetro al modelo User importado de django.contrib.auth.models
    # que maneja Django de forma automática y dentro suyo el parámetro on_delete=models.CASCADE que le indica a Django que si borramos un usuario, se borrarán también todas las entradas de las cuales sea el autor, de ahí lo de cascada, porque el modelo User se lleva los modelos relacionados con él.
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"
        ordering = ['-created']

    def __str__(self):
        return self.title
