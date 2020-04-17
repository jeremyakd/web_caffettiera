from django.db.models import Model, CharField, TextField, DateTimeField

class Page(Model):
    title = CharField(verbose_name="Título", max_length=200)
    content = TextField(verbose_name='Contenido')
    created = DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['title']

    def __str__(self):
        return self.title
