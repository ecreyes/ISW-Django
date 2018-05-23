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
    symbol = forms.ModelChoiceField(queryset=Enterprise.objects.all().order_by('name'))  
    tasa_de_interes = forms.FloatField()
    tiempo_años = forms.IntegerField()
    precio = forms.IntegerField()
    tipo = forms.ChoiceField(choices=TIPO)
    opcion = forms.ChoiceField(choices=OPCION)
    desde = forms.DateField(initial=YESTERDAY)
    hasta = forms.DateField(initial=datetime.date.today)
    
    
