from django.db import models
from cities_light.models import City
from django.db.models.fields import EmailField
from phonenumber_field.modelfields import PhoneNumberField
from applications.core.models import ModelClass

# Create your models here.
class GeneralProfile(ModelClass):
    """
    Perfil general de la página web
    """

    name = models.CharField(verbose_name='Nombre', max_length=50)
    legal_name = models.CharField(verbose_name='Nombre legal', max_length=80, null=True, blank=True)
    nit = models.CharField(verbose_name='NIT', max_length=13, null=True, blank=True)
    #positive_logo = models.ImageField(verbose_name='Logo para fondos positivos', upload_to='profile_logo', blank=True, null=True)
    #negative_logo = models.ImageField(verbose_name='Logo para fondos negativos', upload_to='profile_logo', blank=True, null=True)
    city = models.ForeignKey(City, verbose_name='Ciudad', on_delete=models.SET_NULL, null=True)
    address = models.CharField(verbose_name='Dirección', max_length=120, null=True, blank=True)
    address_2 = models.CharField(verbose_name='Datos adicionales', max_length=120, null=True, blank=True)
    validation_date = models.DateField(verbose_name='Fecha de creación', blank=True, null=True)
    phone = PhoneNumberField(verbose_name='Número telefónico', blank=True, null=True)
    email = models.EmailField(verbose_name='Correo electrónico', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)
    
    class Meta:
        verbose_name = 'Perfil general'
        verbose_name_plural = 'Perfiles generales'
        ordering = ['name']