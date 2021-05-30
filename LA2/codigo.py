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
deltaF = float(input("Ingrese la desviación máxima de frecuencia: "))

"""
Velocidad de bits
"""
f_b=10e3
t_b=1/(f_b) #Tiempo de bit
f_a=f_b/2 #Frecuencia fundamental maxima de entrada binaria 
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





