from django.db import models

class Tipo_producto(models.Model):
    nombre_tipo = models.CharField(max_length=30, verbose_name="Nombre")
    
    def __str__(self):
        return self.nombre_tipo
    
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        db_table = "tipo_producto"
        ordering = ['id']
        
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=30, verbose_name="Nombre de categoria")
    
    def __str__(self):
        return self.nombre_categoria
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = "categoria_producto"
        ordering = ['id']
        
class Ubicacion(models.Model):
    nombre_ubicacion = models.CharField(max_length=30, verbose_name="Nombre")
    
    def __str__(self):
        return self.nombre_ubicacion
    
    class Meta:
        verbose_name = "Ubicacion"
        verbose_name_plural = "Ubicaciones"
        db_table = "ubicacion"
        ordering = ['id']
        
class Productos(models.Model):
    nombre_producto = models.CharField(max_length=30, verbose_name="Nombre")
    imagen_producto = models.ImageField(upload_to='productos/', null=True, verbose_name='Imagen')
    tipo = models.ForeignKey(Tipo_producto, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso")
    nit_proveedor = models.IntegerField(verbose_name="Proveedor")
    existencias = models.IntegerField(verbose_name="Existencias")
    descripcion = models.CharField(max_length=50, verbose_name='descricion')
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    
    def __str__(self):  
        return self.nombre_producto
    
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "prosuctos"
        db_table = "productos"
        ordering = ['id']

class Productos_produccion(models.Model):
    nombre_producto = models.CharField(max_length=30, verbose_name="Nombre")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_entrega = models.DateField(verbose_name="Fecha de entrega")
    duracion_estimada = models.IntegerField(verbose_name="Duracion estimada")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.cantidad
    
    class Meta:
        verbose_name = "Produccion"
        verbose_name_plural = "Producciones"
        db_table = "produccion"
        ordering = ['id']
        

