from django.shortcuts import render
from .forms import FormularioArchivoCsv
from django.forms.widgets import Select, Widget
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse_lazy
from apps.formulario.online import simulacion
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#def handle_uploaded_file(f):
#    with open('some/file/name.csv', 'wb+') as destination: #directorio donde deberia ir el  archivo
#        for chunk in f.chunks():
#            destination.write(chunk)
#cambiar directorio
def handle_uploaded_file(f):
    with open(BASE_DIR + '\\media\\archivo_formulario.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


            
def form_file(request):
    if request.method == 'POST':
        form = FormularioArchivoCsv(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['symbol']
            tasa_de_interes = form.cleaned_data['tasa_de_interes']
            tiempo_años = form.cleaned_data['tiempo_años']
            precio = form.cleaned_data['precio']
            tipo = form.cleaned_data['tipo']
            opcion = form.cleaned_data['opcion']
            handle_uploaded_file(request.FILES['symbol'])
            resultado = simulacion(tiempo_años,tasa_de_interes,precio,100)
            context ={'funcion':resultado[0],'promedio':resultado[1],'valores_trayectoria':resultado[2],'valores_cierre':resultado[3],'dias_i':resultado[4],'num_tray':resultado[5],'lista_prom':resultado[6]}
            return render(request,'formulario/resultado.html',context) #Redirigir a nueva pagina ,agregando los datos obtenidos del formulario como contexto
    else:
        form = FormularioArchivoCsv()
        context = {"form": form}
        return render(request,'formulario/form_file.html',context,RequestContext(request))
