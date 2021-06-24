from django.urls import path
from . import views

app_name = 'Purchases'

urlpatterns = [
    path('proveedores/', views.SupplierList.as_view(), name="supplier_list"),
    path('proveedores/nuevo/', views.SupplierCreate.as_view(), name="supplier_create"),
    path('proveedores/editar/<int:pk>', views.SupplierUpdate.as_view(), name="supplier_update"),
]