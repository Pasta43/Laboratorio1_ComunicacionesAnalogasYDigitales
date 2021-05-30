import math
import numpy as np
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
def moduladora(tren,samples,t_b):
    valores = list()
    for i in range(len(tren)):
        unTiempo=np.linspace(i*t_b,(i+1)*t_b,int(samples/8))
        for t in unTiempo:
            valores.append(tren[i])
    return valores

#ASK
def ASK(f_c,V_c,tren,samples,t_b):
    valores = list()
    w=2*math.pi*f_c
    for i in range(len(tren)):
        unTiempo=np.linspace(i*t_b,(i+1)*t_b,int(samples/8))
        for t in unTiempo:
            valores.append((1+tren[i])*(V_c/2)*math.cos(w*t))
    return valores  

#FSK
def FSK(f_c,V_c,tren,samples,t_b,deltaF):
    valores = list()
    w=2*math.pi*f_c
    for i in range(len(tren)):
        unTiempo=np.linspace(i*t_b,(i+1)*t_b,int(samples/8))
        for t in unTiempo:
            valores.append((V_c)*math.cos(2*math.pi*(f_c + deltaF*tren[i])*t))
    return valores  

#BPSK
def BPSK(f_c,tren,samples,t_b,f_a):
    valores = list()
    w=2*math.pi*f_c
    for i in range(len(tren)):
        unTiempo=np.linspace(i*t_b,(i+1)*t_b,int(samples/8))
        for t in unTiempo:
            valores.append(tren[i]*math.sin(2*math.pi*f_a*t)*math.sin(w*t))
    return valores  

#QPSK
def QPSK(f_c,tren,samples,t_b):
    valores = list()
    w=2*math.pi*f_c
    for i in range(int(len(tren)/2)):
        unTiempo=np.linspace(2*i*t_b,2*(i+1)*t_b,int(samples/4))
        for t in unTiempo:
            valores.append(tren[i]*math.sin(w*t)+tren[i+1]*math.cos(w*t))
    return valores  

