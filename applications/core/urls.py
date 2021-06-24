from django.urls import path
from . import views

app_name = 'Core'

urlpatterns = [
    path('sin_privilegios/', views.NoPrivilegesTemplate.as_view(), name="no_privileges"),
]