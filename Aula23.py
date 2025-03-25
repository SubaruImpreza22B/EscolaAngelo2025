lista_de_numeros = [54, 23, 18, 99, 15]

i=0

while i < len(lista_de_numeros):
    print(lista_de_numeros[i], end=" ")
    i += 1
    print()
    for elemento in lista_de_numeros:
        print(elemento, end= " ")

print()
i = 0
for el in lista_de_numeros:
    print(i, el, end=" ")
    i += 1
    print(f"Indice = {i}, elemento = {el}")

for elemento, indice in enumerate(lista_de_numeros):
    print(elemento) 

for indice, elemento in enumerate(lista_de_numeros):
    print("indice:", indice, "elemento:", elemento)

for numero in range(9):
    print(numero)

for numero in range(1, 9):
    print(numero)

print()
for numero in range(1, 9, 2):
    print(numero)

print()
lista_com_range = list(range(1, 11))
print(lista_com_range)

for letra in "Ciencia de Dados":
    print(letra)

escola = "Angelo Mendes"
print("O indice 7 da string é:", escola[7])

lista = []

texto = "Hoje é dia de Minecraft"
for letra in texto:
    lista.append(letra)
print(lista)
for letra in lista:
    print(letra, end="")

print()

#faça uma lista de numeros de 1 até 20 e some os pares usando range e for e mostre a soma

lista2 = list(range(1, 21))
soma = 0
for numero in lista2:
    if numero % 2 == 0:
        soma += numero

print(f"soma é: {soma}")        
