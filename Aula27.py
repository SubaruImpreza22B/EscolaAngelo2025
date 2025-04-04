# 1. Crie duas variáveis do tipo string, uma contendo “Olá” e outra contendo “Mundo”. Concatene-as e imprima o resultado.
string1 = "Olá"
string2 = "Mundo"
strings = string1 + string2
print(strings)

# 2. Dada a string “Python”, imprima o caractere que está no índice 2.
string = "Python"
character = string[2]
print(character)

# 3. Crie uma string qualquer. Substitua um dos caracteres por outro e imprima a nova string resultante.
string = "Hello"
new_string = string.replace("o", "a")
print(new_string)

# 4. Solicite ao usuário que digite seu nome. Em seguida, imprima o comprimento do nome fornecido.
name = input("Digite seu nome: ")
length = len(name)
print(length)

# 5. Crie uma string que represente uma frase. Verifique se a palavra “gato” está presente na frase e imprima o resultado (verdadeiro ou falso)
phrase = "O gato está dormindo."
contains_gato = "gato" in phrase
print(contains_gato)

# 6. Peça ao usuário que digite uma frase. Conte o número de palavras na frase e imprima o resultado.
sentence = input("Digite uma frase: ")
word_count = len(sentence.split())
print(word_count)

# 7. Crie uma função que receba uma frase como parâmetro e retorne a mesma frase com as palavras invertidas. Por exemplo, “Olá Mundo” deve ser transformado em “Mundo Olá”.
def reverse_words(frase):
    words = frase.split()
    reversed_words = " ".join(reversed(words))
    return reversed_words

frase = input("Digite uma frase: ")
frase_invertida = reverse_words(frase)
print(frase_invertida)

# 8. Solicite ao usuário que digite uma string que contenha espaços em branco no início e no final. Remova esses espaços e imprima a string resultante.
string = input("Digite uma string: ")
trimmed_string = string.strip()
print(trimmed_string)

# 9. Crie uma função que receba um número inteiro e retorne uma string que o represente com separadores de milhares. Por exemplo, para o número 1234567, a função deve retornar “1,234,567”.
def format_number(number):
    formatted_number = "{:,}".format(number)
    return formatted_number

number = int(input("Digite um número inteiro: "))
formatted_number = format_number(number)
print(formatted_number)

# 10. Implemente uma função que receba uma string e um número (chamado de “deslocamento”) como parâmetros e retorne a string cifrada, usando a Cifra de César. Cada letra na string deve ser deslocada pelo número fornecido. Por exemplo, com um deslocamento de 3, “ABC” seria cifrado como “DEF”
def caesar_cipher(string, shift):
    ciphered_string = ""
    for char in string:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            ciphered_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphered_string += ciphered_char
        else:
            ciphered_string += char
    return ciphered_string

string = input("Digite uma string: ")
shift = int(input("Digite o deslocamento: "))
ciphered_string = caesar_cipher(string, shift)
print(ciphered_string)

# 11. Escreva um programa que receba uma palavra ou frase do usuário e determine se ela é um palíndromo ou não. O programa deve ignorar maiúsculas e minúsculas, bem como espaços em branco
def is_palindrome(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]

word_or_phrase = input("Digite uma palavra ou frase: ")
if is_palindrome(word_or_phrase):
    print("É um palíndromo")
else:
    print("Não é um palíndromo")