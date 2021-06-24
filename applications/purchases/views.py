from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from applications.core.views import NoPrivileges, BaseCreateView, BaseUpdateView
from .models import *
from .forms import SupplierForm
# Create your views here.

class SupplierList(NoPrivileges, ListView):
    permission_required = 'purchases.view_supplier'
    model = Supplier
    template_name = 'purchases/lists/supplier_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Proveedores'
        context['entity'] = 'Lista de proveedores'
        return context

class SupplierCreate(BaseCreateView):
    permission_required = "purchases.add_supplier"
    model = Supplier
    template_name = "purchases/forms/supplier_form.html"
    form_class = SupplierForm
    success_url = reverse_lazy('Purchases:supplier_list')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo proveedor'
        context['nombre_boton'] = 'Agregar proveedor'
        context['volver_url'] = reverse_lazy('Purchases:supplier_list')
        context['action'] = 'add'
        return context

class SupplierUpdate(BaseUpdateView):
    permission_required = "purchases.change_supplier"
    model = Supplier
    template_name = "purchases/forms/supplier_form.html"
    form_class = SupplierForm
    success_url = reverse_lazy('Purchases:supplier_list')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar proveedor'
        context['nombre_boton'] = 'Editar proveedor'
        context['volver_url'] = reverse_lazy('Purchases:supplier_list')
        context['action'] = 'edit'
        return context