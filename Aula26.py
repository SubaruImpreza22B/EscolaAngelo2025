 #Você está construindo um sistema de gerenciamento de contatos. Crie um programa que realize as seguintes tarefas:
 
 #  a) Peça ao usuário para digitar seu nome completo.

Nomecompleto = input("Digite seu nome completo: ")

 
 #  b) Concatene “Olá,” com o nome fornecido e exiba o resultado.
 
print(f"Olá, {Nomecompleto}")


 #  c) Conte quantos caracteres existem no nome completo digitado e exiba o resultado.
 
print(f"O nome {Nomecompleto} tem {len(Nomecompleto)} caracteres.")

 #  d) Peça ao usuário para digitar um sobrenome para procurar na string do nome completo.
 
Sobrenome = input("Digite seu sobrenome: ")


 #  e) Verifique se o sobrenome fornecido está presente no nome completo e exiba uma mensagem apropriada.
 
if Sobrenome in Nomecompleto:
    print(f"O sobrenome {Sobrenome} está presente no nome completo.")
else:
    print(f"O sobrenome {Sobrenome} não está presente no nome completo.")

 #  f) Exiba o nome completo em letras maiúsculas.
 
Sobrenome = Sobrenome.upper()
print(Sobrenome)

 #  g) Substitua todas as ocorrências da vogal “a” na string do nome completo pelo caractere ‘4’ e exiba o resultado

while "a" in Nomecompleto:
    Nomecompleto = Nomecompleto.replace("a", "4")
print(Nomecompleto)