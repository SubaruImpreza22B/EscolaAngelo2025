from random import randint as rd

print(rd(0,100))

def dados():
    dado1 = rd(1,20)
    dado2 = rd(1,20)
    return (dado1, dado2)
print(dados())

Jogada = dados()
print(f"O dado 1 deu {Jogada[0]} e o dado 2 deu {Jogada[1]}")
print(f"A soma dos dados é {Jogada[0] + Jogada[1]}")
