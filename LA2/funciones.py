import math
"""
Archivo de funciones 
"""

#Señal Portadora
def portadora(V_c,f_c,tiempo):
    valores = list()
    w_c=2*math.pi*f_c
    for t in tiempo:
        valores.append(V_c*math.cos(w_c*t))
    return valores

#Señal Moduladora
def moduladora(V_m,f_m,tiempo):
    valores = list()
    w_m=2*math.pi*f_m
    for t in tiempo:
        valores.append(V_m*math.sin(w_m*t))
    return valores