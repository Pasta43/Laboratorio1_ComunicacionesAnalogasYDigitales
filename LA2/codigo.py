from math import log
from codigo import Delta_f
import matplotlib.pyplot as plt
import numpy as np
import funciones

samples=2000
"""Captura de caracter ascii"""
valor=input("Digite un caracter del código ASCII: ")
numeroAscii=ord(valor)
binarioAscii=bin(numeroAscii).replace("0b","")
strBinarioAscii=str(binarioAscii)

"""Tren de pulsos para Señal Moduladora """
tren = [int(strBinarioAscii[i:i+1], 2) for i in range(0, len(strBinarioAscii), 1)]
while(len(tren)<8):
    tren.insert(0,0)
print(tren)
for i in range(len(tren)):
    if(tren[i]==0):
        tren[i]=-1
print("Datos Señal Portadora")

"""
Amplitud y frecuencia señal Portadora 
"""
V_c = float(input("Ingrese la amplitud de la señal portadora: "))
f_c = float(input("Ingrese la frecuencia de la señal portadora: "))
k1 = float(input("Ingrese la sensibilidad de la desviación: "))
f_b = float(input("Ingrese la rapidez de bits: "))
"""
Velocidad de bits
"""
deltaF=k1
t_b=1/(f_b) #Tiempo de bit
f_a=f_b/2 #Frecuencia fundamental maxima de entrada binaria 
h = deltaF/f_a #Factor h 
tiempo= np.linspace(0,2*t_b,samples)

# 2. Visualizar las señales Portadora, Moduladora y Modulada.
# Vector Tiempo 

"""
Tren de pulsos
"""

"""
Señal portadora
"""
señalPortadora=funciones.portadora(V_c,f_c,tiempo)
fig, ax = plt.subplots()
ax.plot(tiempo, señalPortadora,label='Señal portadora')  # Plot some data on the axes.# ... and some more.
ax.set_xlabel('Tiempo')  # Add an x-label to the axes.
ax.set_ylabel('Señal portadora')  # Add a y-label to the axes.
ax.set_title("Señal portadora")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()

"""
Señal Moduladora
"""
señalModuladora=funciones.moduladora(tren,samples,t_b)
fig, ax = plt.subplots()
ax.plot(tiempo, señalModuladora,label='Señal Moduladora')  # Plot some data on the axes.# ... and some more.
ax.set_xlabel('Tiempo')  # Add an x-label to the axes.
ax.set_ylabel('Señal Moduladora')  # Add a y-label to the axes.
ax.set_title("Señal Moduladora")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()

"""
ASK
"""
ASK=funciones.ASK(f_c,V_c,tren,samples,t_b)
fig, ax = plt.subplots()
ax.plot(tiempo, ASK,label='ASK')  # Plot some data on the axes.# ... and some more.
ax.set_xlabel('Tiempo')  # Add an x-label to the axes.
ax.set_ylabel('ASK')  # Add a y-label to the axes.
ax.set_title("ASK")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()


"""
FSK
"""
FSK=funciones.FSK(f_c,V_c,tren,samples,t_b,deltaF)
fig, ax = plt.subplots()
ax.plot(tiempo, FSK,label='FSK')  # Plot some data on the axes.# ... and some more.
ax.set_xlabel('Tiempo')  # Add an x-label to the axes.
ax.set_ylabel('FSK')  # Add a y-label to the axes.
ax.set_title("FSK")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()

"""
BPSK
"""
BPSK=funciones.BPSK(f_c,tren,samples,t_b,f_a)
fig, ax = plt.subplots()
ax.plot(tiempo, BPSK,label='BPSK')  # Plot some data on the axes.# ... and some more.
ax.set_xlabel('Tiempo')  # Add an x-label to the axes.
ax.set_ylabel('BPSK')  # Add a y-label to the axes.
ax.set_title("BPSK")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()


"""
QPSK
"""
QPSK=funciones.QPSK(f_c,tren,samples,t_b)
fig, ax = plt.subplots()
ax.plot(tiempo, QPSK,label='QPSK')  # Plot some data on the axes.# ... and some more.
ax.set_xlabel('Tiempo')  # Add an x-label to the axes.
ax.set_ylabel('QPSK')  # Add a y-label to the axes.
ax.set_title("QPSK")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()


"""
BESSEL
"""
fig, ax = plt.subplots()

J=funciones.funcionDeBessel(h)
amplitudesEspectro= list()
dominioFrecuencia=list()
for n in range(len(J)):
    if(n!=0):
        amplitudesEspectro.append(J[n]*V_c)
        dominioFrecuencia.append(f_c+n*f_b)  
    amplitudesEspectro.append(J[n]*V_c)
    dominioFrecuencia.append(f_c-n*f_b)

# Gráficas
ax.stem(dominioFrecuencia, amplitudesEspectro,label="Espectro de amplitud")
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Volts [V]')
plt.show()

#Diagrama de constelación BPSK
fig, ax = plt.subplots()
vectores = np.array([[-1,0], [1,0]])
origin = [0,0] # origin point
colores=['r','y']
labels=['0','1']
for vector, label,color in zip(vectores, labels,colores):
    plt.quiver(origin[0],origin[1],vector[0],vector[1],scale=7,label=label,color=color)
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
ax.set_xlabel(r'$\sin(\omega_ct)$')  # Add an x-label to the axes.
ax.set_ylabel(r'$\cos(\omega_ct)$')  # Add a y-label to the axes.
ax.set_title("Diagrama de constelación BPSK")  # Add a title to the axes.
ax.legend()
plt.show()


#Diagrama de constelación QPSK
fig, ax = plt.subplots()
vectores = np.array([[1,1], [-1,1], [-1,-1],[1,-1]])
origin = [0,0] # origin point
colores=['r','g','b','y']
labels=['11','01','00','10']
for vector, label,color in zip(vectores, labels,colores):
    plt.quiver(origin[0],origin[1],vector[0],vector[1],scale=7,label=label,color=color)
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
ax.set_xlabel(r'$\sin(\omega_ct)$')  # Add an x-label to the axes.
ax.set_ylabel(r'$\cos(\omega_ct)$')  # Add a y-label to the axes.
ax.set_title("Diagrama de constelación QPSK")  # Add a title to the axes.
ax.legend()
plt.show()

"""
Visualización de datos
"""

#Desviación máxima de frecuencia 
print("La desviación máxima de frecuencia es: ±",deltaF )

#Sensibilidad de la desviación
print("La sensibilidad de la desviación es: ",k1)

#Indice de modulación
print("El indice de modualción es: ",h)

#Frecuencias de marca y espacio
f_s = (f_c - deltaF)
print("La frecuencia de espacio es: ",f_s, "Hz")

f_m = (f_c + deltaF)
print("La frecuencia de marca es: ",f_m,"Hz")

#Frecuencia de bits
print("La frecuencia de bits es: ",f_b)

#Tiempo de bits
print("El tiempo de bits es: ", t_b)

#Ancho de banda minimo BPSK 
print("El ancho de banda minimo es: ", f_b)

#Ancho de banda minimo QPSK 
B = f_b/2
print("El ancho de banda minimo para QPSK es: ", B)

#Ancho de banda minimo FSK 
B = 2*(deltaF + f_b)
print("El ancho de banda minimo para FSK es: ", B)

#Condiciones M-aria
M=2
N=int(log(M,2))
print("Codificación M-aria para BPSK M=",M,"N=",N)
M=4
N=int(log(M,2))
print("Codificación M-aria P QPSK  M=",M,"N=",N)




