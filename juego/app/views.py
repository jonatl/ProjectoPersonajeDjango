from .models import Invocadore,Inventarie
from .forms import ContactameForm,InvocadorForm,InventariooForm
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    Personajes=Invocadore.objects.all()
    data={
        'Personajes':Personajes
    }
    return render(request,'app/home.html',data) #Busca el html para que se muestre

def galeria(request):
    return render(request,'app/galeria.html')

def contactoformview(request):
    data={
        'form':ContactameForm()
    }
    if request.method=='POST':
        formulario=ContactameForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Contacto Guardado"
        else:
            data["mensaje"]="Contacto no guardado"
            data["form"]=formulario
    return render(request, 'app/contacton.html',data)

def AgregarFormView(request):
    data={
        'formdos':InvocadorForm()
    }
    if request.method=='POST':
        formulario=InvocadorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="personaje Guardado"
        else:
            data["formdos"]=formulario
    return render(request, 'app/personajetl/agregar.html',data)

def AgregarInventarioFormView(request):
    data={
        'forminventario':InventariooForm()
    }
    if request.method=='POST':
        formulario=InventariooForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="item Guardado"
        else:
            data["mensaje"]="item no guardado"
            data["forminventario"]=formulario
    return render(request, 'app/inventariotl/agregarinv.html',data)

def Peleeaa(request):
    return render(request,'app/Batalla.html')

def ListarPersonajes(request):
    listado=Invocadore.objects.all()
    data={
        'ListarPersonaje':listado
    }
    return render(request, 'app/personajetl/listar.html',data)

def ListarInventario(request):
    listado=Inventarie.objects.all()
    data={
        'ListarInventario':listado
    }
    return render(request, 'app/inventariotl/listarinv.html',data)

#def ListadoInventario(request):
    Lis=Inventarie.objects.all()
    data={
        'ListaINventario':Lis
    }
    return render(request,'app/home.html',data) 