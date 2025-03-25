# EXERCÍCIOS FOR

#  1.Faça um programa que imprima cada elemento da lista [28, 9, 22, -31, -3, -31, 10, 32, 10, 2] usando o for.

lista_numeros = [28, 9, 22, -31, -3, -31, 10, 32, 10, 2]
for numero in lista_numeros:
    print(numero)

print()
#  2. Faça um programa que imprima cada elemento da lista [3, 8, 30, 8, 19, -12, -2, -1, -7, -48] usando o for com range.

lista_de_numeros2 = [3, 8, 30, 8, 19, -12, -2, -1, -7, -48]
for numero in range(len(lista_de_numeros2)):
    print(lista_de_numeros2[numero])

print()
#  3. Crie uma lista com 10 números inteiros e faça um programa que imprima cada elemento da lista usando o for

lista_de_numeros3 = [75, 52, 91, 40, 69, 24, 14, 111, 3, 13]
for numero in lista_de_numeros3:
    print(numero)

#  4. Crie uma lista com 10 números inteiros e faça um programa que imprima cada elemento da lista usando o for com range

lista_de_numeros3 = [75, 52, 91, 40, 69, 24, 14, 111, 3, 13]
for numero in range(len(lista_de_numeros3)):
    print(lista_de_numeros3[numero])

print()
# 5. Faça um programa que imprima todos os itens da lista [28, 9, 22, -31, -3, -31, 10, 32, 10, 2] usando while e compare-o com o exercício 1.

lista_numero4 = [28, 9, 22, -31, -3, -31, 10, 32, 10, 2]
i = 0
while i < len(lista_numero4):
    print(lista_numero4[i])
    i += 1 

print()
#  6. Faça um programa que imprima todos os números de 5 a 0 usando o for.

lista_vazia = []
for numero in range(5, -1, -1):
    lista_vazia.append(numero)
print(lista_vazia)

print()
#  7. Faça um programa que peça para o usuário digitar um número n e imprima uma lista com todos os números de 0 a n-1

n = int(input("Digite um número: "))
lista_vazia2 = []
for numero in range(n):
    lista_vazia2.append(numero)
print(lista_vazia2)


print()
# 8. Faça um programa que imprima o maior número da lista [-8, -6, 3, -1, 7], sem usar o método max(). 

lista_numeros5 = [-8, -6, 3, -1, 7]
maior_numero = lista_numeros5[0]
for numero in lista_numeros5:
    if numero > maior_numero:
        maior_numero = numero
print(maior_numero)

print()
# 9. Agora, usando o método max(), faça um programa que imprima os três maiores números da lista [2, 9, -5, 2, -8, 4, -9, -5, 4, 1].

lista_numeros6 = [2, 9, -5, 2, -8, 4, -9, -5, 4, 1]
maiores_numeros = sorted(lista_numeros6, reverse=True)[:3]
for numero in maiores_numeros:
    print(numero)
