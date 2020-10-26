# -*- coding: utf-8 -*-
"""
Spyder Editor
Script throught generated a matriz with dimension of 15x100
This matriz is the first step to generate algorithms solutions
"""
import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt
import time
import dist


print('Porfavor defina el tamanio de la matriz a utilizar')
print('Valor por Default: 15X100')
change = int(input('Quiere cambiar el tamanio\n 1)yes\n 2)No\n  :'))

if change == 1:
    row = int(input('Ingrese el numero de filas: '))
    col = int(input('Ingrese el numero de columnas: ' ))
else:
    row = 100
    col = 14
    
#matriz = np.empty((row,col))
matriz = []
val=[]

city = [[1,1],[1,7],[2,3],[2,5],[3,2],[4,4],[5,1],[6,6],[7,3],[9,8],[10,5],[12,3],[13,1],[13,6]]
listaX = []
listaY = []
distancia = []
SumaDistancia = 0
ganador = []
indices =[]
reproduccion = []
matrizHijos = []

for j in range(1,(col+1)):
    val.append(j)

for i in range(row):
  #  matriz[i] = random.sample(val, col)
    matriz.append(random.sample(val, col))
    print(matriz[i])
    for road in range(len(matriz[0])):  #####################create the road to visit the cities
        listaX.append(city[int(matriz[i][road]-1)][0])
        listaY.append(city[int(matriz[i][road]-1)][1])
            
    for cit in city: #######################################create a grphic and draw the cities points
        plt.plot(cit[0],cit[1], 'o')
        
    ##############################################################Aptitude Function
    ########################################################Calculate distance and add to list distancia
    for indice in range(len(listaX)-1):
        SumaDistancia = SumaDistancia + dist.distance(listaX[indice],listaY[indice],listaX[indice+1],listaY[indice+1])
        
    distancia.append(SumaDistancia)
    
    plt.plot(listaX, listaY)
    plt.grid()
    plt.show()
    listaX = []
    listaY = []
    SumaDistancia = 0
    
for cien in range(100):
    torneo = []
    ################################################################################## TORNEOS
    ##################################################################################
    #################################################################################
    for tor in range(5):
        x = random.randint(0,99)
        torneo.append([distancia[x],x])
        
    ganador = [min(torneo)]
    ################################################################################Reproduccion
    reproduccion = matriz[ganador[0][1]]
    metodo = random.randint(1,2)
    #print('metodo:', metodo, 'iteracion', cien, 'ganador:', ganador[0][1])
    ###reproduccion 1:
    
    if metodo == 1:
        elementos = random.randint(1,6)
        posicion = random.randint(1,6)
        posicion2 = posicion + 6
        mitad1 = []
        mitad2 = []
        if (7-posicion) >= elementos:
            for i in range(elementos):
                mitad1.append(reproduccion[posicion+i])
                mitad2.append(reproduccion[posicion2+i])
                
            for j in range(elementos):
                reproduccion[posicion2+i] = mitad1[i]
                reproduccion[posicion+i] = mitad2[i]
        
        matrizHijos.append(reproduccion)
        #print(reproduccion)
        reproduccion = []

    ###Reproduccion 2:
    if metodo == 2:
            
        while True:
            elementos = random.randint(1,12)
            posicion = random.randint(1,12)
            derecha = []
            invertida = []
            if (13-posicion) >= elementos:
                for i in range(elementos):
                    derecha.append(reproduccion[posicion + i])
                        
                invertida = derecha[::-1]
                
                for j in range(elementos):
                    reproduccion[posicion + j] = invertida[j]
    
                matrizHijos.append(reproduccion)
                #print(reproduccion)
                reproduccion = []
                break
