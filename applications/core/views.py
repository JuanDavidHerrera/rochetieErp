from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render


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
            self.login_url='Core:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))

# Create your views here.
