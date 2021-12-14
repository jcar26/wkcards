from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TipoUsuario(models.Model):
    usuario_tipo = models.CharField(max_length=40)
    idusuario = models.ManyToManyField(User, default=None)


