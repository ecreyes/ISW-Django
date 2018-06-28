from django import forms
from .models import Enterprise
from django.forms.widgets import Select, Widget
import datetime

TIPO = (
    ('Compra','Compra'),
    ('Venta','Venta'),
)

OPCION = (
    ('Europea','Europea'),
    ('Americana','Americana'),
    )

YESTERDAY  = datetime.datetime.now() - datetime.timedelta(days = 1)
YESTERDAY = YESTERDAY.strftime("%d/%m/%Y")
      
class TrayectoriaForm(forms.Form):
    symbol = forms.ModelChoiceField(queryset=Enterprise.objects.all().order_by('name'),widget=forms.Select(
            attrs={
                'style': 'border-color: green;',
                'placeholder': 'Opcion',
                'class': 'form-control'
            }
        )
    )  
    tasa_de_interes = forms.FloatField(widget=forms.NumberInput(
            attrs={
                'style': 'border-color: green;',
                'placeholder': 'Tasa de Interes',
                'class': 'form-control'
            }
        )
    )
    tiempo_años = forms.IntegerField(widget=forms.NumberInput(
            attrs={
                'style': 'border-color: green;',
                'placeholder': 'Tiempo en Años',
                'class': 'form-control'
            }
        )
    )
    precio = forms.IntegerField(widget=forms.NumberInput(
            attrs={
                'style': 'border-color: green;',
                'placeholder': 'Precio',
                'class': 'form-control'
            }
        )
    )
    tipo = forms.ChoiceField(choices=TIPO,widget=forms.Select(
            attrs={
                'style': 'border-color: green;',
                'placeholder': 'Tipo',
                'class': 'form-control'
            }
        )
    )
    opcion = forms.ChoiceField(choices=OPCION,widget=forms.Select(
            attrs={
                'style': 'border-color: green;',
                'placeholder': 'Opcion',
                'class': 'form-control'
            }
        )
    )
    desde = forms.DateField(widget=forms.DateInput(
            attrs={
                'style': 'border-color: green;',
                'placeholder': 'Desde - Ex: 23/04/2016',
                'class': 'form-control'
            }
        )
    )
    hasta = forms.DateField(widget=forms.DateInput(
            attrs={
                'style': 'border-color: green;',
                'placeholder': 'Hasta - Ex: 26/04/2016',
                'class': 'form-control'
            }
        )
    )
    
    
