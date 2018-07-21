from django.shortcuts import render
from .forms import TrayectoriaForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import Enterprise
from apps.trayectoria.online import simulacion


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
            if(desde.day<10):
                desde_dia = '0'+str(desde.day)
            else:
                desde_dia = str(desde.day)
            if(desde.month<10):
                desde_mes = '0'+str(desde.month)
            else:
                desde_mes = str(desde.month)
            if(hasta.day<10):
                hasta_dia = '0'+str(hasta.day)
            else:
                hasta_dia = str(hasta.day)
            if(hasta.month<10):
                hasta_mes = '0'+str(hasta.month)
            else:
                hasta_mes = str(hasta.month)
            desde_string = str(desde.year)+desde_mes+desde_dia
            hasta_string = str(hasta.year)+hasta_mes+hasta_dia

            desde_output = desde_dia+"/"+desde_mes+"/"+str(desde.year)
            hasta_output = hasta_dia+"/"+hasta_mes+"/"+str(hasta.year)

            resultado = simulacion(simbol,desde_string,hasta_string,tiempo_años,tasa_de_interes,precio,100)
            #[funcion, media_trayectorias, valores_trayectorias,valores_cierre,dias_i,lista_num_tray,lista_prom_tray,desde,hasta,i_anios,i_tasa,i_precio,nombre]
            context ={'funcion':resultado[0],'promedio':resultado[1],'valores_trayectoria':resultado[2],'valores_cierre':resultado[3],'dias_i':resultado[4],'num_tray':resultado[5],'lista_prom':resultado[6],
            'desde_dia':desde_output, 'hasta_dia':hasta_output, 'tiempo_años':tiempo_años, 'tasa_de_interes':tasa_de_interes, 'precio_i':precio, 'nombre_empresa':name}
            return render(request,'trayectoria/resultado.html',context) #Redirigir a nueva pagina ,agregando los datos obtenidos del formulario como contexto
    else:
        form = TrayectoriaForm()
        context = {"form": form}
        return render(request,'trayectoria/index.html',context,RequestContext(request))
