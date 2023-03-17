from django.contrib import admin
from .models import Inventarie, Invocadore, contacto
# Register your models here.
class PersonajeListado(admin.ModelAdmin):
    list_display=["name","nivel","vida","resistencia","fuerza","daño","tipo"]
    search_fields=["name"]
    list_filter=["tipo"]

class InventarioListado(admin.ModelAdmin):
    list_display=["name","cantidad","fk"]
    search_fields=["name"]
    list_filter=["fk"]

class ContactoListado(admin.ModelAdmin):
    list_display=["nombre","correo","importante"]

admin.site.register(Invocadore,PersonajeListado)
admin.site.register(Inventarie,InventarioListado)
admin.site.register(contacto,ContactoListado)
