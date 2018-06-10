from yahoo_quote_download import yqd
import numpy as np
import online
import matplotlib.pyplot as plt


funcion, media_trayectoria,valores_trayectorias,valores_max,valores_cierre,dias_i = online.simulacion('FB','20180102','20180329',0.08,0.025,60,1000)
print(funcion)
print(media_trayectoria)

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
    plt.axhline(y=np.mean(valores_max),linewidth=4, color='b',label="Promedio Trayectorias")
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
val_tra_maxVSnum_iter(valores_max)
