from django.contrib import admin

# Register your models here.

from gestionTarjetas.models import TipoTarjeta,Publicacion,Tarjeta,Comentarios


class TipoTarjetaAdmin(admin.ModelAdmin):
    list_display = ("tarjeta_tipo",)

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ("fecha_publciacion","idtarjeta","idusuario")
    list_per_page = 20

class TarjetaAdmin(admin.ModelAdmin):
    list_display = ("titulo","descripcion","idtipotarjeta")
    list_per_page = 20

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ("comentario","idtarjeta","idusuario")
    list_per_page = 10

admin.site.register(TipoTarjeta,TipoTarjetaAdmin) #pasas tu modelo mas la clase admin
admin.site.register(Publicacion,PublicacionAdmin)
admin.site.register(Tarjeta,TarjetaAdmin)
admin.site.register(Comentarios,ComentariosAdmin)
