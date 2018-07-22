###OFFLINE####
import numpy as np
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


#Funcion auxiliar para transformar el formato de fecha YYYY-MM-DD a una en formato DD/MM/YYYY
def formato_fecha(fecha):
        aux = fecha.split("-")
        fecha_form = aux[2]+"/"+aux[1]+"/"+aux[0]
        return fecha_form


#Simulación de una trayectoria
###INPUTS###
#s_1: valor trayectoria actual
#conta: contador de iteracion
#d: numero de dias
#r: tasa libre de riesgo
#sigma: media aritmetica de valores de cierre en escala logaritmica
#t: tiempo en años
###OUPUTS: Ver en el codigo ###
def trayectoria(s_1,conta,d,r,sigma,t):
        epsilon = np.random.normal()
        delta_s = r*s_1*t + sigma*s_1*epsilon*np.sqrt(t)
        sn_1 = s_1 + delta_s #Nuevo valor de trayectoria
        conta = conta + 1
        if conta == d:
                return sn_1 #Retornar a ultimo valor de trayectoria calculada
        return trayectoria(sn_1,conta,d,r,sigma,t) #Si aun no termina el contador, seguir recursivamente

#Simulacion de varias trayectorias
###INPUTS###
#nombre: nombre de la empresa
#desde y hasta: fechas en formato 'AAAAMMDD' que representan un intervalo de tiempo para hacer la simulacion
#i_anios: tiempo en años que se quieren estimar
#i_tasa: valor de la tasa
#i_precio: precio inicial
#num_tray: numero de trayectorias a genzerar
###OUTPUTS###
#funcion: valor final de la simulacion
#media_trayectorias: promedio/media de las trayectorias obtenidas
#valores_trayectorias: lista de los valores de las trayectorias
def simulacion(i_anios,i_tasa,i_precio, num_tray,tipo_derecho):
        #obtengo los datos de FB , desde-hasta
        #lista contiene todos los valores de cierre
        dias_i = []
        valores_cierre = []
        datos = open(BASE_DIR + '\\media\\archivo_formulario.csv',"r")

        contador = 0
        for i in datos:
                lista = i.rstrip('\n').split(",")
                if (lista[4] != 'Close'):
                        if contador == 0:
                                desde = lista[0]
                                contador = 1
                        valores_cierre.append(float(lista[4]))
                        a = str((lista[0]))
                        hasta = lista[0]
                        dias_i.append(a)
        datos.close()
        #lista contiene todos los valores del ln(j/j-1)
        valores_log = []
        for j in range(1,len(valores_cierre)):
                calculo = (np.log(valores_cierre[j]))/(np.log(valores_cierre[j-1]))
                valores_log.append(calculo)

        #valores a utilizar
        trayectorias = num_tray
        d = int(i_anios*360) #numero de dias
        t = i_anios/1000 #tiempo en años
        r = i_tasa *d/360 #tasa libre de riesgo
        s = valores_cierre #lista que se utilizan para las simulaciones
        RC = valores_log #lista que se utilizan para las simulaciones (valores logaritmicos)
        precio = i_precio #precio estimado
        sigma = np.std(valores_log)
        #resultados obtenidos
        valores_trayectorias = []
        valores_max = []


        #simulacion de todas las trayectorias requeridas

        for i in range(1,trayectorias):
                #simulacion de 1 trayectoria
                sn_1 = trayectoria(s[len(s)-1],0,d,r,sigma,t)
                valores_trayectorias.append(sn_1) #agrego ultimo valor de la trayectoria simulada
                #Calculo de acuerdo al tipo de derecho de opcion escojida
                if tipo_derecho == 'Compra':
                        valores_max.append(np.maximum(sn_1-precio,0)) #agrego maximo entre 0 y la diferencia entre el ultimo valor de trayectoria simulada y el precio
                if tipo_derecho == 'Venta':
                        valores_max.append(np.maximum(precio-sn_1,0)) #agrego maximo entre 0 y la diferencia entre el precio y el ultimo valor de trayectoria simulada 
                #inicializo valores para futuras trayectorias.
                sigma = np.std(valores_log)
                RC = valores_log

        esperanza = np.mean(valores_max)
        funcion = np.exp(-i_tasa*i_anios)*esperanza
        media_trayectorias = np.mean(valores_trayectorias)
        lista_num_tray = list(range(0,len(valores_trayectorias)))
        lista_prom_tray = [media_trayectorias] * len(valores_trayectorias)

        desde_fo = formato_fecha(desde)
        hasta_fo = formato_fecha(hasta)


        return [funcion, media_trayectorias, valores_trayectorias,valores_cierre,dias_i,lista_num_tray,lista_prom_tray,desde_fo,hasta_fo]


#nombre,desde,hasta,i_anios,i_tasa,i_precio, num_tray
#funcion, media_trayectoria,valores_trayectorias,valores_max,valores_cierre,dias_i = simulacion('AAPL','20170720','20180720',1,0.01,60,1000)
#print(funcion)
#print(media_trayectoria)
