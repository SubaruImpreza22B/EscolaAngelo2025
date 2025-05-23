# EXERCÍCIOS WHILE

#  1. Adivinhação de números:
#  • Criem uma lista com 10 números.
#  • Peçam ao usuário para adivinhar um número da lista.
#  • Usem um loop while para continuar pedindo adivinhações até que o usuário acerte.

lista_sorteio = [99, 13, 23, 45, 65, 12, 7, 67, 1, 56]
input_usuario = int(input("Digite um número: "))
while input_usuario not in lista_sorteio:
    print("Tente novamente!")
    input_usuario = int(input("Digite um número: "))
if input_usuario in lista_sorteio:
    print("Parabéns, você acertou!")    

#  2. Contagem regressiva:
 # • Criem uma lista de contagem regressiva de 10 a 1.
  #• Usem um loop while para imprimir cada número da lista
X = 0 
while X <= 10:
    print(X)
    X += 1


# 3. Adição de números:
#  • Criem uma lista vazia para armazenar números.
#  • Peçam ao usuário para fornecer números e os adicionem à lista.
#  • Continuem pedindo números até que o usuário decida parar.
lista_vazia = []

while True:
    input_usuario = int(input("Digite um número: "))
    lista_vazia.append(input_usuario)
    print(lista_vazia)

#  4.Média de notas:
#  • Criem uma lista vazia para armazenar notas.
#  • Peçam ao usuário para fornecer notas e as adicionem à lista.
#  • Calculem e imprimam a média das notas quando o usuário decidir parar
lista_de_notas = []
while True:
    input_usuario = int(input("Digite uma nota: "))
    lista_de_notas.append(input_usuario)
    print(lista_de_notas)
    continuar = input("Deseja continuar? (s/n): ")
    if continuar == "n":
        media = sum(lista_de_notas) / len(lista_de_notas)
        print(f"A média das notas é: {media}")
        break    

# 5.Busca em lista:
#  • Criem uma lista de cinco nomes.
#  • Peçam ao usuário para digitar um nome.
#  • Usem um loop while para verificar se o nome está na 
# lista e informar o resultado.

lista_de_nomes = ["Maria", "Felipe", "Carlos", "Arthur", "João"]
input_usuario = input("Digite um nome: ")
while input_usuario not in lista_de_nomes:
    print("Nome não encontrado!")
    input_usuario = input("Digite um nome: ")
    if input_usuario in lista_de_nomes:
        print("Nome encontrado!")
        break
    

#  6. Contador de números:
 # • Solicitem ao usuário um número inicial.
  #• Usem um loop while para imprimir os números de 1 até o 
 #número fornecido pelo usuário.
  #• Exibam uma mensagem indicando que o loop terminou

input_usuario = int(input("Digite um número: "))
X = 0 + 1
while X <= input_usuario:
    print(X)
    X += 1 
    if X == input_usuario:
        print("Loop terminado!")
        break