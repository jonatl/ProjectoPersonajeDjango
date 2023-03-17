from django.db import models
operaciones=[
    [0,"Queja"],
    [1,"Sugerencia"],
    [2,"Quiero ponerme en contacto con el creador amen"],
    [3,"Felicitaciones"]
    ]
# Create your models here.
class Invocadore(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    vida = models.IntegerField(blank=True, null=True)
    resistencia = models.IntegerField(blank=True, null=True)
    fuerza = models.IntegerField(blank=True, null=True)
    daño = models.FloatField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    img=models.ImageField(upload_to="personaje",blank=False,null=False)
    def __str__(self):
        return self.name
    
    
class Inventarie(models.Model):
    fk = models.ForeignKey(Invocadore, on_delete=models.CASCADE)
    cantidad = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return str(self.fk)

class contacto(models.Model):
    nombre=models.CharField(max_length=30)
    correo=models.EmailField()
    consulta=models.IntegerField(choices=operaciones)
    mensaje=models.TextField()
    importante=models.BooleanField()