from django.contrib import admin

# Register your models here.

from gestionUsuarios.models import TipoUsuario


class TipoUsuarioAdmin(admin.ModelAdmin):
    list_display = ("usuario_tipo",)



admin.site.register(TipoUsuario,TipoUsuarioAdmin)
