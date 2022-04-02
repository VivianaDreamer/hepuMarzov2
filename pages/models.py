from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Pages(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de actualización", auto_now=True)

    class Meta:
        verbose_name = "página"
        ordering = ['title']

    def __str__(self):
        return self.title