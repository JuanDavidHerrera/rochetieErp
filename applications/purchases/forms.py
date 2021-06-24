from django import forms
from cities_light.models import City
from .models import Supplier

class SupplierForm(forms.ModelForm):

    city = forms.ModelChoiceField(
        queryset= City.objects.filter(country__name='Colombia').order_by('region', 'name')
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'

        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['city'].empty_label = "Seleccione una ciudad"

    class Meta:
        model = Supplier
        exclude = ['creation_date', 'modification_date', 'creator_user', 'modifier_user']
        widgets = {
           'name' : forms.TextInput(
                attrs= {
                    'placeholder' : 'Ingrese el nombre del proveedor',
                }
            ),
            'nit' : forms.TextInput(
                attrs= {
                    'placeholder' : 'Ingrese el NIT del proveedor',
                }
            ),
            'address' : forms.Textarea(
                attrs= {
                    'placeholder' : 'Ingrese la dirección de la empresa',
                    'rows' : 2,
                }
            ),
            'address_2' : forms.TextInput(
                attrs= {
                    'placeholder' : 'Incluya los datos adicionales que considere necesarios',
                }
            ),
            'phone' : forms.TextInput(
                attrs= {
                    'placeholder' : 'Ejemplo: (321) 123-4567',
                }
            ),
            'email' : forms.TextInput(
                attrs= {
                    'placeholder' : 'Ejemplo: contacto@empresa.com',
                }
            ),
            'observations' : forms.Textarea(
                attrs= {
                    'placeholder' : 'Ingrese las observaciones que considere necesarias para este proveedor. Por ejemplo: pedido minimo, descuentos por cantidad, etc',
                    'rows' : 2,
                }
            ),
        }