#Colocar em uma lista uma na outra só pares  e outra impares

from random import randint as r

valores = [[], []]

for x in range(10):
    valor = r(1,100)
    if valor % 2  == 0:
        indice = 0
    else:
        indice = 1
    if valor not in valores[indice]:
        valores[indice].append(valor)

print(valores)
print(f"Lista de pares: {sorted(valores[0])}")
print(f"Lista de ímpares: {sorted(valores[1])}")

     

