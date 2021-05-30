import funciones
valor=input("Digite un caracter del código ASCII: ")
numeroAscii=ord(valor)
binarioAscii=bin(numeroAscii).replace("0b","")
strBinarioAscii=str(binarioAscii)
numbers = [int(strBinarioAscii[i:i+1], 2) for i in range(0, len(strBinarioAscii), 1)]
print (numbers)

while(len(numbers)<8):
    numbers.insert(0,0)
print(numbers)
