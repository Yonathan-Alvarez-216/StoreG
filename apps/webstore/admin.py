from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

class resourceproductos(resources.ModelResource):
    class Meta:
        model = productos

class Adminproductos(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['modelo']
    list_display = ['descripcion']
    resource_class = resourceproductos

admin.site.register(productos, Adminproductos)


class resourcecategorias(resources.ModelResource):
    class Meta:
        model = categorias

class Admincategorias(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    resource_class = resourcecategorias

admin.site.register(categorias, Admincategorias)

class resourceforo(resources.ModelResource):
    class Meta:
        model = foro

class Adminforo(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ['contenido','link','fecha']
    resource_class = resourceforo

admin.site.register(foro, Adminforo)

