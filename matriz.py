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
    
matriz = np.empty((row,col))
val=[]

city = [[1,1],[1,7],[2,3],[2,5],[3,2],[4,4],[5,1],[6,6],[7,3],[9,8],[10,5],[12,3],[13,1],[13,6]]
listaX = []
listaY = []

for j in range(1,(col+1)):
    val.append(j)

for i in range(row):
    matriz[i] = random.sample(val, col)
    print(matriz[i])
    for road in range(len(matriz[0])):  #####################create the road to visit the cities
        listaX.append(city[int(matriz[i][road]-1)][0])
        listaY.append(city[int(matriz[i][road]-1)][1])
        
        
    for cit in city: #######################################create a grphic and draw the cities points
        plt.plot(cit[0],cit[1], 'o')
        
    plt.plot(listaX, listaY)
    plt.grid()
    plt.show()
    listaX = []
    listaY = []
