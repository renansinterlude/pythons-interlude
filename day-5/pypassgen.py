# Projeto Gerador de Senhas
import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_']

print("Bem-vindo ao Gerador de Senhas PyPassGen!")
nr_letras = int(input("Quantas letras você gostaria em sua senha?\n")) 
nr_simbolos = int(input(f"Quantos símbolos você gostaria?\n"))
nr_numeros = int(input(f"Quantos números você gostaria?\n"))
tamanho = nr_letras + nr_simbolos + nr_numeros

senha = ""

for caractere in range(0, nr_letras):
  senha += random.choice(letras)

for caractere in range(0, nr_simbolos):
  senha += random.choice(simbolos)

for caractere in range(0, nr_numeros):
  senha += random.choice(numeros)

senha_embaralhada = list(senha)
random.shuffle(senha_embaralhada)
senha_embaralhada = ''.join(senha_embaralhada)

print("Senha simples: " + senha)
print("Senha embaralhada (recomendada): " + senha_embaralhada)
