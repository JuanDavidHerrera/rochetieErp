from typing import ClassVar
from django.db import models
from django.db.models.base import Model
from applications.core.models import ModelClass
from cities_light.models import City
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Supplier(ModelClass):
    name = models.CharField(max_length=100, verbose_name='Nombre', unique=True)
    nit = models.CharField(max_length=13, verbose_name='NIT', unique=True, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Ciudad', null=True, blank=True)
    address = models.CharField(verbose_name='Dirección', max_length=120, null=True, blank=True)
    address_2 = models.CharField(verbose_name='Datos adicionales', max_length=120, null=True, blank=True)
    phone = PhoneNumberField(verbose_name='Número telefónico', blank=True, null=True)
    email = models.EmailField(verbose_name='Correo electrónico', null=True, blank=True)
    observations = models.TextField(verbose_name='Observaciones', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['name']
