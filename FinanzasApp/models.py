from django.db import models

from django.utils import timezone

class FormaDePago(models.Model):
    nombre = models.CharField(max_length = 40)
    credito = models.BooleanField() #Indica si se trata de una forma de pago en crédito (A diferencia de pagos inmediatos como debito, efectivo o transferencia)
    descripcion = models.CharField(max_length = 200)

class Ingreso(models.Model):
    nombreIngreso = models.CharField('Título Ingreso', max_length = 40)
    descripcion = models.CharField(max_length = 200)
    monto = models.FloatField()
    titularNombre = models.CharField('Titular', max_length = 40) #Nombre de la parsona que recibió el ingreso
    fecha = models.DateField(help_text="Format: YYYY-MM-DD", default=timezone.now)

class Egreso(models.Model):
    nombreEgreso = models.CharField('Título Engreso', max_length = 40)
    descripcion = models.CharField(max_length = 200)
    monto = models.FloatField()
    titularNombre = models.CharField('Titular', max_length = 40) #Nombre de la parsona que generó el gasto
    formaDePago = models.CharField(max_length = 40, default='Efectivo')
    fecha = models.DateField(help_text="Formato: YYYY-MM-DD", default=timezone.now)

class Persona(models.Model):
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    dni = models.IntegerField('DNI') # Para que muestre "DNI" en CRUD en lugar de "Dni"
    email = models.EmailField()