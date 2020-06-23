from django.db import models

class Link(models.Model):
    key = models.SlugField(verbose_name='Nombre clave', max_length=200, unique=True)
    name = models.CharField(verbose_name='Red social', max_length=200)
    url = models.URLField(verbose_name='URL', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ['name']

    def __str__(self):
        return self.name