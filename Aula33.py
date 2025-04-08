#compreensão de listas

lista = []
for numero in range(1, 11):
    lista.append(numero)
print(lista)

lista2 = [numero for numero in range(1, 11)]
print(lista2)

print()

lista3 = []
for numero in range(1,11):
    if numero % 2 == 0:
        lista3.append(numero)
print(f"lista de números pares: {lista3}")

print()

lista4 = [numero for numero in range(1,11) if numero % 2 == 0]

print(f"lista de números pares: {lista4}")

print()

lista5 = []
for numero in range(1,11):
    if numero % 2 != 0:
        numero = numero ** 2
        lista5.append(numero)
print(f"lista de números ímpares ao quadrado: {lista5}")

lista6 = [numero ** 2 for numero in range(1,11) if numero % 2 != 0]

print([(x, y, x + y ) for x in range(3) for y in range(3) if (x+y) % 2 == 0])