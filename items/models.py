from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    
class ObjetoPerdido(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    encontrado = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    objeto = models.ForeignKey(ObjetoPerdido, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.usuario.username} en {self.objeto.titulo}'
