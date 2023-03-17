from django.contrib import admin
from django.urls import path
from.views import home,galeria,contactoformview,AgregarFormView,Peleeaa,AgregarInventarioFormView,ListarPersonajes,ListarInventario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"), #en la raiz del sitio se va a vargar el view llamado "home"
    path('galeria/',galeria,name="galeria"),
    path('contacto/',contactoformview,name="contacto"),
    path('agregar/',AgregarFormView,name="agregar"),
    path('Inventario/',AgregarInventarioFormView,name="aggInventario"),
    path('Batalla/',Peleeaa,name="Batalla"),
    path('listar/',ListarPersonajes,name="listar"),
    path('ListInv/',ListarInventario,name="ListInv"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)