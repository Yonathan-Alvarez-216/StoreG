from django.db import models

# Create your models here.
class marca(models.Model):
    pk_marca = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)


class categorias(models.Model):
    pk_categorias = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=150, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)


class foro(models.Model):
    pk_foro = models.AutoField(primary_key=True, null=False, blank=False)
    titulo = models.CharField(max_length=200, null=False, blank=False)
    contenido = models.TextField(null=False, blank=False)
    link = models.URLField(max_length=250)
    fecha = models.DateField(auto_now=False, auto_now_add=True, null=False, blank=False)


class productos(models.Model):
    pk_productos = models.AutoField(primary_key=True, null=False, blank=False)
    fk_categorias = models.ManyToManyField(categorias, blank=False)
    fk_marca = models.ManyToManyField(marca, blank=False)
    modelo = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=False,blank=False)
    fk_foro = models.ManyToManyField(foro, blank=False)


