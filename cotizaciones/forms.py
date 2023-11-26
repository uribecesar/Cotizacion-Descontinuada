from django import forms
from .models import *
from django.utils.translation import ugettext_lazy as _
from .widgets import FenChenDatePickerInput


class FormCotizacion(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ('cliente', 'fecha', 'distrito', 'direccion','telefono','email', 'adicional')
        widgets = {
            'cliente': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")',
                    }),
            'fecha': FenChenDatePickerInput(
                attrs={
                    'class' : 'form-control',
                }
            ),
            'distrito': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'direccion': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'telefono': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'email': forms.EmailInput(
                attrs={
                    'class' : 'form-control',
                }
            ),
            'adicional': forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows': '3',
                }
            ),
            }
        labels = {
            'cliente': _('Nombre de cliente'),
            'fecha': _('Fecha'),
            'distrito': _('Distrito'),
            'direccion': _('Dirección'),
            'telefono': _('Número de Telefono'),
            'email': _('Correo electrónico'),
            'adicional': _('Detalles adicionales'),
        }

class FormItemCotizacion(forms.ModelForm):
    class Meta:
        model = ItemCotizacion
        fields = ('descripcion', 'cantidad', 'unidad', 'val_unit')
        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'class' : 'form-control mb-3',
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'cantidad': forms.NumberInput(
                attrs={
                    'class' : 'form-control mb-3',
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'unidad': forms.Select(
                attrs={
                    'class' : 'form-control mb-3',
                }
            ),
            'val_unit': forms.NumberInput(
                attrs={
                    'class' : 'form-control mb-3',
                    'oninvalid': 'this.setCustomValidity("Sólo número entero o decimal, ejemplo: 10.50")',
                    'oninput': 'setCustomValidity("")',
                    }),
            }
        labels = {
            'descripcion': _('Descripción'),
            'cantidad': _('Cantidad'),
            'unidad': _('Tipo de unidad'),
            'val_unit': _('Valor unitario'),
        }
