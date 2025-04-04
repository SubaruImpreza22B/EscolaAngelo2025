#Outras estruturas de dados: tuplas, conjuntos e dicionários

r = range(1, 9)
print(r)

for item in r:
    print(item)

lista = list(r)
print(lista)

lista_vazia = []
lista_vazia = list()

tupla = ()
tupla = tuple()

tupla = tuple(r)

print(tupla)

lista = ["Gustavo", "Felipe", "Gabriel", "Marcio"]
tupla = ("Gustavo", "Felipe", "Gabriel", "Marcio")
print(lista)
print(tupla) 

lista.append("João")
print(lista)

#tupla não pode ser alterada

tupla = tupla + ("João",)
print(tupla)

conjunto = {}
conjunto = set(r)
print(conjunto)

conjunto.add(865)
print(conjunto)

dicionario = {}
dicionario = dict()

dicionario = {"SP":"São Paulo", "RJ":"Rio de Janeiro","ES":"Espírito Santo"}
print(dicionario)

print(dicionario["SP"])


dicionario_nomes = {1:"Gustavo", 2:"Felipe", 3:"Gabriel", 4:"Marcio"}

print(dicionario_nomes[1])

dicionario_paises = {55:"BR", 1:"US", 43:"JP"}
print(dicionario_paises[55])
