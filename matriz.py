# -*- coding: utf-8 -*-
"""
Spyder Editor

Script throught generated a matriz with dimension of 15x100
This matriz is the first step to generate algorithms solutions
"""
import numpy as np
import random

print('Porfavor defina el tamanio de la matriz a utilizar')
print('Valor por Default: 15X100')
change = int(input('Quiere cambiar el tamanio\n 1)yes\n 2)No\n  :'))

if change == 1:
    row = int(input('Ingrese el numero de filas: '))
    col = int(input('Ingrese el numero de columnas: ' ))
else:
    row = 100
    col = 15
    
matriz = np.empty((row,col))
val=[]

for j in range(1,(col+1)):
    val.append(j)

for i in range(row):
    matriz[i] = random.sample(val, col)
    print(matriz[i])
