from django import forms
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
      
class FormularioArchivoCsv(forms.Form):
    symbol = forms.FileField()
    tasa_de_interes = forms.FloatField()
    tiempo_años = forms.IntegerField()
    precio = forms.IntegerField()
    tipo = forms.ChoiceField(choices=TIPO)
    opcion = forms.ChoiceField(choices=OPCION)
    desde = forms.DateField(initial=YESTERDAY)
    hasta = forms.DateField(initial=datetime.date.today)

    
