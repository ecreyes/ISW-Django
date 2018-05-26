from django.shortcuts import render
from .forms import FormularioArchivoCsv
from django.forms.widgets import Select, Widget
from django.http import HttpResponseRedirect
from django.template import RequestContext

def handle_uploaded_file(f):
    with open('some/file/name.csv', 'wb+') as destination: #directorio donde deberia ir el  archivo
        for chunk in f.chunks():
            destination.write(chunk)

            
def form_file(request):
    if request.method == 'POST':
        form = TrayectoriaForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['symbol'])
            tasa_de_interes = form.cleaned_data['tasa_de_interes']
            tiempo_años = form.cleaned_data['tiempo_años']
            precio = form.cleaned_data['precio']
            tipo = form.cleaned_data['tipo']
            opcion = form.cleaned_data['opcion']
            desde = form.cleaned_data['desde']
            hasta = form.cleaned_data['hasta']
            return HttpResponseRedirect('/graficos/') #Redirigir a misma pagina que 'trayectorias'
    else:
        form = FormularioArchivoCsv()
        context = {"form": form}
        return render(request,'formulario/form_file.html',context,RequestContext(request))
