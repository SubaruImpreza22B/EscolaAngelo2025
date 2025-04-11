from random import randint

tupla1 = (randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20))
print(tupla1)

numeros = ()
i = 1
while i <= 6:
    numero = (randint(1, 20),)
    if numero not in numeros:
        numeros += numero
    i += 1
print(numeros)
print(tuple(sorted(numeros)))