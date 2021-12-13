from django.db import models
from categoria.models import Categoria

# Create your models here.
class Post(models.Model):
        titulo = models.CharField(max_length=200, null=False, blank=False)
        autor = models.CharField(max_length=100, null=False, blank=False)
        texto = models.TextField()
        categoria = models.ForeignKey(Categoria, on_delete = models.PROTECT)
        

        def __str__(self):
            return self.titulo + self.autor