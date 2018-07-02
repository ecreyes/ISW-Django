from yahoo_quote_download import yqd
import numpy as np
import online
import matplotlib.pyplot as plt
from datetime import timedelta

#nombre,desde,hasta,i_anios,i_tasa,i_precio, num_tray
funcion, media_trayectoria,valores_trayectorias,valores_max,valores_cierre,dias_i = online.simulacion('FB','20180102','20180329',1,0.01,60,1000)
print(funcion)
print(media_trayectoria)

'''
def año_bisiesto(a):
    if(a % 4 == 0 and a % 100 != 0 or a % 400 == 0):
        return 1
    else:
        return 0
def dia_siguiente(dia_a):
    año = int(dia_a[0] + dia_a[1] + dia_a[2] + dia_a[3])
    mes = int(dia_a[4] + dia_a[5])
    dia = int(dia_a[6] + dia_a[7])
    bisiesto = año_bisiesto(año)
    if bisiesto == 1:
        if dia == 31:
            if mes == 12:
                año2 = str(año + 1)
                mes2 = '01'
                dia2 = '01'
            else:
                
                mes2 = str(mes + 1)
                if len(mes2) == 1:
                    mes2 = '0' + mes2
                dia2 = '01'
                año2 = str(año)
        elif dia == 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
                mes2 = str(mes + 1)
                if len(mes2) == 1:
                    mes2 = '0' + mes2
                dia2 = '01'
                año2 = str(año)
        elif dia == 29 and (mes == 2):
                mes2 = str(mes + 1)
                if len(mes2) == 1:
                    mes2 = '0' + mes2
                dia2 = '01'
                año2 = str(año)
        else:
            dia2 = str(dia + 1)
            if len(dia2) == 1:
                dia2 = '0' + dia2
            año2 = str(año)
            mes2 = str(mes)
            if len(mes2) == 1:
                mes2 = '0' + mes2
    else:
        if dia == 31:
            if mes == 12:
                año2 = str(año + 1)
                mes2 = '01'
                dia2 = '01'
            else:
                mes2 = str(mes + 1)
                if len(mes2) == 1:
                    mes2 = '0' + mes2
                dia2 = '01'
                año2 = str(año)
        elif dia == 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
                mes2 = str(mes + 1)
                if len(mes2) == 1:
                    mes2 = '0' + mes
                dia2 = '01'
                año2 = str(año)
        elif dia == 28 and (mes == 2):
            mes2 = str(mes + 1)
            if len(mes2) == 1:
                    mes2 = '0' + mes2
            dia2 = '01'
            año2 = str(año)
        else:
            dia2 = str(dia + 1)
            if len(dia2) == 1:
                dia2 = '0' + dia2
            año2 = str(año)
            mes2 = str(mes)
            if len(mes2) == 1:
                mes2 = '0' + mes2
    print(año2 + mes2+ dia2)
def lista_fechas(dia_i, i_anios):
    lista_dias = []
    print(i_anios)
lista_fechas('20180329',0.12)
#año_bisiesto(2018)
'''
def val_traVSnum_iter(valores_trayectorias,media_trayectoria):
    num_iter = range(0,len(valores_trayectorias))
    plt.plot(num_iter, valores_trayectorias, 'ro',label="Valor por iteración")
    plt.axhline(y=media_trayectoria,linewidth=4, color='b',label="Promedio Trayectorias")
    plt.axis([0, len(num_iter), min(valores_trayectorias), max(valores_trayectorias)])
    plt.title("Num. Iteracion VS Valor de trayectoria")
    plt.xlabel("Num. Iteracion")
    plt.ylabel("Valor de trayectoria")

    plt.grid()
    plt.legend(loc='best')
    plt.show()

def val_tra_maxVSnum_iter(valores_max):
    num_iter = range(0,len(valores_max))
    plt.plot(num_iter, valores_max, 'ro',label="Valor máximo (entre 0 y valor-precio) por iteración")
    plt.axhline(y=np.mean(valores_max),linewidth=4, color='b',label="Promedio valores máximos")
    plt.axis([0, len(num_iter), min(valores_max), max(valores_max)])
    plt.title("Num. Iteracion VS Valor máximo trayectoria")
    plt.xlabel("Num. Iteracion")
    plt.ylabel("Valor máximo trayectoria")

    plt.grid()
    plt.legend(loc='best')
    plt.show()

def tiempoVSval_cierre(valores_cierre,dias_i):
    
    plt.plot(dias_i, valores_cierre, 'ro--',label="Valor de cierre")
    plt.xticks(rotation=90)
    plt.title("Dias VS Valores cierre inciales")
    plt.xlabel("Dias")
    plt.ylabel("Valor de cierre")
    
    plt.grid()
    plt.legend(loc='best')
    plt.show()


#val_traVSnum_iter(valores_trayectorias,media_trayectoria)
#tiempoVSval_cierre(valores_cierre,dias_i)
#val_tra_maxVSnum_iter(valores_max)
