# -*- coding: utf-8 -*-
"""
Spyder Editor

Script throught generated a matriz with dimension of 15x100
This matriz is the first step to generate algorithms solutions
"""
import numpy as np

print('Porfavor deefina el tamanio de la matriz a utilizar')
print('Valor por Default: 15X100')
change = int(input('Quiere cambiar el tamanio\n 1)yes\n 2)No\n  :'))

if change == 1:
    col = int(input('Ingrese el numero de columnas: ' ))
    row = int(input('Ingrese el numero de filas: '))
else:
    col = 15
    row = 100
