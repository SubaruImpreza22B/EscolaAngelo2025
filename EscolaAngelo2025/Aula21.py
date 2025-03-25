lista_numeros = [10, 20, 30, 40]
lista_numeros.insert(4, 50)
print(lista_numeros)

lista_de_frutas = ["maça", "banana", "uva"]
lista_de_frutas.insert(1, "laranja")
print(lista_de_frutas)

lista_de_animais = ["cachorro", "gato", "passaro", "cachorro"]
while "cachorro" in lista_de_animais:
    lista_de_animais.remove("cachorro")
print(lista_de_animais)

lista_nomes = ["Alice", "Bob", "Charlie", "David"]
print(f"O nome removido será: {lista_nomes[2]}")
lista_nomes.remove("Charlie")
print(lista_nomes)

lista_cores = ["vermelo", "azul", "verde", "amarelo", "azul"]
print(f"O índice do primeiro azul é: {lista_cores.index('azul')}")

lista_numeros_repetidos = [1,2,3,2,4,2,5,2]
print(lista_numeros_repetidos)
count = lista_numeros_repetidos.count(2) 
print(f"o número 2 aparecem: {count} vezes")

lista_desordenada = [50, 20, 80, 10, 40]
lista_desordenada.sort()
print(lista_desordenada)

lista_invertida = ["maça", "banana", "laranja", "uva"]
lista_invertida.reverse()
print(lista_invertida)
