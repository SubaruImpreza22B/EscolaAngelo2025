from random import randint as rd
numero = set()
def MegaSena():
    numero1 = rd(1,20)
    if numero1 not in numero:
        numero.add(numero1)
    else:
        numero1 = rd(1,20)
    numero2 = rd(1,20)
    if numero2 not in numero:
        numero.add(numero2)
    else:
        numero2 = rd(1,20)
    numero3 = rd(1,20)
    if numero3 not in numero:
        numero.add(numero3)
    else:
        numero3 = rd(1,20)
    numero4 = rd(1,20)
    if numero4 not in numero:
        numero.add(numero4)
    else:
        numero4 = rd(1,20)
    numero5 = rd(1,20)
    if numero5 not in numero:
        numero.add(numero5)
    else:
        numero5 = rd(1,20)
    numero6 = rd(1,20)
    if numero6 not in numero:
        numero.add(numero6)
    else:
        numero6 = rd(1,20)
    return numero


Jogada = input("digite 6 numeros diferentes entre 1 a 20:")
Jogada = Jogada.split()
Jogada = [int(num) for num in Jogada]
if Jogada == numero:
    print("você ganhou")
else:
    print("tente novamente")

print(MegaSena())




