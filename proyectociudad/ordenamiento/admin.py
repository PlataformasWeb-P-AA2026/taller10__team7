from django.contrib import admin
from ordenamiento.models import Barrio, Parroquia,PresidenteBarrio 
# Register your models here.

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    search_fields = ('nombre', 'tipo')
admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'num_viviendas', 'num_parques','num_edificios_residenciales')
    search_fields = ('nombre',)
admin.site.register(Barrio, BarrioAdmin)

class PresidenteBarrioAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nickname', 'edad','profesion')
    search_fields = ('cedula','nickname')
admin.site.register(PresidenteBarrio, PresidenteBarrioAdmin)