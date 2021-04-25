import matplotlib.pyplot as plt
import numpy as np


import funciones


# 1.Permitir ingresar amplitudes y frecuencias para las señales portadora y moduladora. 
print(chr(27)+"[1;33m"+"Por favor ingrese los datos solicitados para las señales]")

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

print("Índice de Modulación")
"""
Indice de modulación Onda Modulada y espectro de frecuencias Bessel
"""
m = float(input("Ingrese el índice de modulación: "))
R= float(input("Ingrese el valor de la resistencia de carga : "))

# 2. Visualizar las señales Portadora, Moduladora y Modulada.
# Vector Tiempo 
T_m=1/(f_m)
tiempo= np.linspace(0,2*T_m,2000)
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


"""
Generación gráfica Onda Modulada PM
"""
ondaModuladaPM=funciones.moduladaPM(V_c,m,f_c,f_m,tiempo)
fig, ax = plt.subplots()
ax.plot(tiempo, ondaModuladaPM,label='Onda Modulada PMS')  # Plot some data on the axes.# ... and some more.
ax.set_xlabel('Tiempo')  # Add an x-label to the axes.
ax.set_ylabel('Onda modulada PM')  # Add a y-label to the axes.
ax.set_title("Onda modulada PM")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()


"""
Generación gráfica Onda Modulada FM
"""

ondaModuladaFM=funciones.moduladaFM(V_c,m,f_c,f_m,tiempo)
fig, ax = plt.subplots()
ax.plot(tiempo, ondaModuladaFM,label='Onda Modulada FM')  # Plot some data on the axes.# ... and some more.
ax.set_xlabel('Tiempo')  # Add an x-label to the axes.
ax.set_ylabel('Onda Modulada FM')  # Add a y-label to the axes.
ax.set_title("Onda Modulada FM")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()


# 3. Espectro de frecuencias Bessel  

"""
Generación gráfica Espectro de frecuencias
"""
fig, ax = plt.subplots()

J=funciones.funcionDeBessel(m)
amplitudesEspectro= list()
dominioFrecuencia=list()
for n in range(len(J)):
    if(n!=0):
        amplitudesEspectro.append(J[n]*V_c)
        dominioFrecuencia.append(f_c+n*f_m)  
    amplitudesEspectro.append(J[n]*V_c)
    dominioFrecuencia.append(f_c-n*f_m)

# Gráficas
ax.stem(dominioFrecuencia, amplitudesEspectro,label="Espectro de amplitud")
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Volts [V]')

plt.show()

# 4. Visualización de datos
"""
Sensibilidad a la desviación
"""
print(chr(27)+"[1;33m"+"Sensibilidad a la desviación")

K = m/(V_m)
print("Sensibilidad a la desviación PM es: ",K)


K1 = (m*f_m)/V_m
print("Sensibilidad a la desviación FM es: ",K1)

"""
Desviación
"""
print(chr(27)+"[1;33m"+ "Desviación")
Delta_theta = (K * V_m)
print("Desviación PM es: ",Delta_theta)


Delta_f = (K1 * V_m)
print("desviación PM es: ",Delta_f)

"""
Indice de modulación
"""
print(chr(27)+"[1;33m"+ "Índice de modulación")
print("Índice de modulación es: ",m)

"""
Porcentaje de modulación
"""
print(chr(27)+"[1;33m"+"Porcentaje de modulación")
M = m*100

print("Porcentaje de modulación es: ",M,"%")

"""
Componentes Portadora y pares de frecuencia laterales
"""
print(chr(27)+"[1;33m"+ "Componentes Portadora y pares de frecuencia laterales")
print(J)

"""
Ancho de banda
"""
print(chr(27)+"[1;33m"+ "Ancho de Banda")
n = len(J)-1 
B = 2*n*f_m
print("EL ancho de banda es: ",B,"Hertz")

"""
Ancho de banda mínimo
"""
print(chr(27)+ "[1;33m"+"Ancho de banda mínimo")
B_min = 2*(Delta_f+f_m)
print("El ancho de banda mínimo es: ",B_min,"Hertz")

"""
Relación de desviación para FM
"""
print(chr(27)+ "[1;33m"+"Relación de desviación para FM")
DR = Delta_f/f_m

print("La relación de desviación para FM: ",DR)


"""
Potencia promedio de la portadora 
"""
print(chr(27)+"[1;33m"+ "Potencia promedio de la portadora")

P_c = (V_c)**2/(2*R)

print("La potencia promedio de la portadora es: ",P_c, "watts")


"""
Potencia de los componentes laterales
"""
print(chr(27)+"[1;33m"+"Potencia de los componentes laterales")


print("La potencia de los componentes laterales es: ")
for n in range(len(amplitudesEspectro)):
    p=amplitudesEspectro[n]**2/R
    print("P_",n,"= ",p," watts")


"""
Potencia total
"""
print(chr(27)+"[1;33m"+ "Potencia total")
P_t = P_c*1+(m**2)/2 

print("La potencia total es: ",P_t,"watts")





