import matplotlib.pyplot as plt
import numpy as np


import funciones


# 1.Permitir ingresar amplitudes y frecuencias para las señales portadora y moduladora. 
print(chr(27)+"Por favor ingrese los datos solicitados para las señales")

print("Datos Señal Portadora")
"""
Amplitud y frecuencia señal Portadora
"""
V_c = float(input("Ingrese la amplitud de la señal portadora: "))
f_c = float(input("Ingrese la frecuencia de la señal portadora: "))

print("Datos Señal Moduladora")
"""
Amplitud y frecuencia señal Moduladora
"""
V_m = float(input("Ingrese la amplitud de la señal moduladora: "))
f_m = float(input("Ingrese la frecuencia de la señal moduladora: "))

"""
Indice de modulación
"""
print("Datos indice de modulación")
m = float(input("Ingrese el indice de modulación: "))

# 2. Visualizar las señales Portadora, Moduladora y Modulada.
# Vector Tiempo 
tiempo= np.linspace(0,00.1,2000)
"""
Generación gráfica Señal Moduladora
"""
señalModuladora=funciones.moduladora(V_m,f_m,tiempo)
fig, ax = plt.subplots()
ax.plot(tiempo, señalModuladora,label='Señal moduladora')  # Plot some data on the axes.# ... and some more.
ax.set_xlabel('Tiempo')  # Add an x-label to the axes.
ax.set_ylabel('Señal moduladora')  # Add a y-label to the axes.
ax.set_title("Señal moduladora")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
 
"""
Generación gráfica Señal Portadora
"""
señalPortadora=funciones.portadora(V_c,f_c,tiempo)
fig, ax = plt.subplots()
ax.plot(tiempo, señalPortadora,label='Señal portadora')  # Plot some data on the axes.# ... and some more.
ax.set_xlabel('Tiempo')  # Add an x-label to the axes.
ax.set_ylabel('Señal portadora')  # Add a y-label to the axes.
ax.set_title("Señal portadora")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()


# 2. Visualizar las señales Portadora, Moduladora y Modulada.



