from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class TipoTarjeta(models.Model):
    tarjeta_tipo = models.CharField(max_length=50)

class Tarjeta(models.Model):
    titulo = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=350)
    foto = models.ImageField(upload_to="imgTarjetas",null=True)
    idtipotarjeta = models.ForeignKey(TipoTarjeta,on_delete=models.CASCADE)

class Publicacion(models.Model):
    fecha_publciacion = models.DateField(auto_now=True,editable=False,blank=True)
    idtarjeta = models.ForeignKey(Tarjeta,on_delete=models.CASCADE)
    idusuario = models.ForeignKey(User, default=None,on_delete=models.CASCADE)

class Comentarios(models.Model):
    comentario = models.CharField(max_length=250)
    idtarjeta = models.ForeignKey(Tarjeta,on_delete=models.CASCADE)
    idusuario = models.ForeignKey(User, default=None,on_delete=models.CASCADE)

class Lista(models.Model):
    titulo = models.CharField(max_length=25)
    idusuario = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    tarjeta_lista = models.ManyToManyField(Tarjeta) #muchos a muchos lista_tarjeta

class Califiacion(models.Model):
    putucion = models.IntegerField()
    idtarjeta = models.ForeignKey(Tarjeta,on_delete=models.CASCADE)
    idusuario = models.ForeignKey(User,default=None,on_delete=models.CASCADE)


