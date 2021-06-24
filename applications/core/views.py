from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)


#Este mixin es para validar los formularios que se hacen desde una ventana modal
class MixinFormInvalid:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

#Esta clase controla el login y los permisos que tienen los usuarios. Además, hereda el MixinFormInvalid
class NoPrivileges(LoginRequiredMixin, PermissionRequiredMixin, MixinFormInvalid):
    login_url = 'Core:login'
    #Para que no se ponga la pantalla en blanco
    raise_exception = False
    redirect_field_name="redirect_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='Core:no_privileges'
        return HttpResponseRedirect(reverse_lazy(self.login_url))

class NoPrivilegesTemplate(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('Core:login')
    template_name = 'core/no_privileges.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Sin permisos'
        context['entity'] = 'Sin permisos'
        return context

#Vistas genéricas
class BaseCreateView(SuccessMessageMixin, NoPrivileges, CreateView):
    success_message="Registro agregado con éxito"
    
    def form_valid(self, form):
        form.instance.usuarioCrea = self.request.user
        return super().form_valid(form)

class BaseUpdateView(SuccessMessageMixin, NoPrivileges, UpdateView):
    success_message="Registro actualizado con éxito"
    
    def form_valid(self, form):
        form.instance.usuarioMod = self.request.user
        return super().form_valid(form)
