from django.db import models
from django.contrib.auth.models import User

class Persona(models.Model):
	nombre=models.CharField(max_length=30)
	apellido=models.CharField(max_length=30)
	correo=models.EmailField()
	direccion=models.CharField(max_length=30)
	idPersona=models.BigIntegerField(unique=True)
	telefono=models.CharField(max_length=20)
	user = models.OneToOneField(User, null=True)
	def __unicode__(self):
		return unicode(self.idPersona)    

class Proveedor(models.Model):
	idProveedor=models.IntegerField(unique=True)
	direccionProveedor=models.CharField(max_length=30,null=True)
	nombreProveedor=models.CharField(max_length=50,null=True)
	telefono=models.CharField(max_length=20,null=True)
	def __unicode__(self):
		return unicode(self.nombreProveedor)

class Categoria(models.Model):
	nombreCategoria=models.CharField(max_length=50,unique=True)
	def __unicode__(self):
		return unicode(self.nombreCategoria)

class Producto(models.Model):
	numeroReferencia=models.IntegerField(unique=True)
	nombreProducto=models.CharField(max_length=49)
	marca=models.CharField(max_length=30,blank=True)
	existencias=models.IntegerField(default=0)
	existenciaMinima=models.IntegerField(default=0)
	descripcion=models.TextField(default="Sin descripcion")
	precio=models.BigIntegerField()
	proveedor=models.ForeignKey(Proveedor,null=True)
	categorias=models.ManyToManyField(Categoria);
	def __unicode__(self):
		return unicode(self.nombreProducto)

class Canasta(models.Model):
	operario=models.OneToOneField(User,null=True)
	def __unicode__(self):
		return unicode(self.operario)
	def calcularValorTotal():
		pass

class DetalleVenta(models.Model):
	canasta=models.ForeignKey(Canasta,null=True)
	cantidad=models.IntegerField(default=1)
	producto=models.ForeignKey(Producto,null=True)
	def __unicode__(self):
		return unicode(self.producto)