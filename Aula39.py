import random 

print(random.randint(1,9))
print()

print ("olá")

def mensagem():
    print ("olá mundo")

mensagem()

def mensagem(texto):
    print (texto)
mensagem("eu sou a lenda!")

def mensagem (texto, numero):
    print (texto, numero)

def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado
print(soma(7,9))

def dobrar(lista):
    indice = 0
    while indice < len(lista):
        lista[indice] *= 2
        indice += 1
valores = [7,9 ,2 ,4 ,1 ,3, 0]

print(valores)
dobrar(valores)
print(valores)

