from django.db import models

# Create your models here.



class categorias(models.Model):
    pk_categorias = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=150, null=False, blank=False)


class foro(models.Model):
    pk_foro = models.AutoField(primary_key=True, null=False, blank=False)
    titulo = models.CharField(max_length=200, null=False, blank=False)
    contenido = models.TextField(null=False, blank=False)
    link = models.URLField(max_length=250)
    fecha = models.DateField(auto_now=False, auto_now_add=True, null=False, blank=False)


class productos(models.Model):
    pk_productos = models.AutoField(primary_key=True, null=False, blank=False)
    modelo = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=False,blank=False)
    precio = models.BigIntegerField(null=False, blank=False)
    img=models.URLField(max_length=8000, blank=False, null=False,default='https://i.ibb.co/w7qB1Zf/Jake.png')
    fk_categorias = models.ForeignKey(categorias, null=False, blank=False, on_delete=models.CASCADE)
    fk_foro = models.ForeignKey(foro, null=False, blank=False, on_delete=models.CASCADE)




