from django.shortcuts import render
from .forms import TrayectoriaForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import Enterprise


# Create your views here.

def index(request):

    if request.method == 'POST':
        form = TrayectoriaForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['symbol']
            simbol = (Enterprise.objects.get(name=name)).symbol
            tasa_de_interes = form.cleaned_data['tasa_de_interes']
            tiempo_años = form.cleaned_data['tiempo_años']
            precio = form.cleaned_data['precio']
            tipo = form.cleaned_data['tipo']
            opcion = form.cleaned_data['opcion']
            desde = form.cleaned_data['desde']
            hasta = form.cleaned_data['hasta']
            return HttpResponseRedirect('/graficos/') #Redirigir a nueva pagina ,agregando los datos obtenidos del formulario como contexto
    else:
        form = TrayectoriaForm()
        context = {"form": form}
        return render(request,'trayectoria/index.html',context,RequestContext(request))
