import math
"""
Archivo de funciones periódicas
"""
#Señal Moduladora
def moduladora(V_m,f_m,tiempo):
    valores = list()
    w_m=2*math.pi*f_m
    for t in tiempo:
        valores.append(V_m*math.sin(w_m*t))
    return valores


#Señal Portadora
def portadora(V_c,f_c,tiempo):
    valores = list()
    w_c=2*math.pi*f_c
    for t in tiempo:
        valores.append(V_c*math.cos(w_c*t))
    return valores


#Onda Modulada FM
def moduladaFM(V_c,m,f_c,f_m,tiempo):
    valores = list()
    w_c=2*math.pi*f_c
    w_m=2*math.pi*f_m
    for t in tiempo:
        valores.append(V_c*math.cos[w_c*t + m*math.sin(w_m*t)])
    return valores

#Onda Modulada PM
def moduladaPM(V_c,m,f_c,f_m,tiempo):
    valores = list()
    w_c=2*math.pi*f_c
    w_m=2*math.pi*f_m
    for t in tiempo:
        valores.append(V_c*math.cos[w_c*t + m*math.cos(w_m*t)])
    return valores

#Función de Bessel
def funcionDeBessel(m):
    J=list()
    n=0
    continuar=True
    while(continuar):
        J.append(0.0)
        s=0
        for s in range(80):
            J[n]+=(((-1)**s)*((m/2)**(2*s)))/((math.factorial(s))*math.factorial(n+s))
        J[n]=J[n]*((m/2)**n)
        if(abs(J[n])<0.01):
            J.pop()
            continuar=False
        else:
            n+=1
    return J


