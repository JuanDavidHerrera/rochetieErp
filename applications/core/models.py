from django.db import models
from django.contrib.auth.models import AbstractUser
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.
class CustomUser(AbstractUser):
    """
    Clase para poner campos adicionales en el modelo User de Django
    """

    profile_pic = models.ImageField(verbose_name='Foto de perfil', upload_to='profile_pics', null=True, blank=True)
    
class ModelClass(models.Model):
    """
    Clase de la que heredaran todos los modelos de la aplicación
    """

    status = models.BooleanField(verbose_name='Estado', default=True)
    creation_date = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    modification_date = models.DateTimeField(verbose_name='Fecha de modificación', auto_now=True)

    creator_user = UserForeignKey(verbose_name='Usuario creador', auto_user_add=True, related_name='+')
    modifier_user = UserForeignKey(verbose_name='Último usuario que modificó', auto_user=True, related_name='+')

    class Meta:
        abstract = True