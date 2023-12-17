import random
import sys
import arte
from palavras import lista_palavras

# Escolhendo palavra
palavra = random.choice(lista_palavras)

# Iniciando vida
vidas = 6

#Iniciando string de letras erradas
letras_erradas = ''

# Iniciando display
display = []
for _ in range(len(palavra)):
    display.append("_")

# Função ganhou
def ganhou():
    return not '_' in display

# Logo
print(arte.logo + "\n")


while not ganhou():
    # Entrada de letra
    letra_escolhida = input("Adivinhe uma letra: ").lower()
    
    # Limpando tela (específico pro Online GDB)
    print("\033c",end='')
    
    # Verifica se letra já foi escolhida
    if letra_escolhida in display:
        print(f"Você já escolheu a letra '{letra_escolhida}'.")
    
    # ACERTO: substituindo espaços do display
    for i, letra in enumerate(palavra):
        if letra == letra_escolhida:
            display[i] = letra_escolhida
    
    # ERRO: verificando se a letra escolhida existe na palavra e subtraindo 1 vida se não
    if letra_escolhida not in palavra:
        print(f"A letra '{letra_escolhida}' não existe na palavra. Você perdeu uma vida.")
        letras_erradas += letra_escolhida + " "
        vidas -= 1
    
    # IMPRESSÃO: 
    print(f"{' '.join(display)}") # Imprimindo display
    print(arte.stages[vidas]) # Imprimindo estágios
    print(letras_erradas + "\n") # Imprimindo letras erradas
    
    # DERROTA: verificando se o usuário perdeu todas as vidas
    if vidas == 0:
        print("Você perdeu.")
        print(f"A palavra era: {palavra}")
        sys.exit()
    
print("Você ganhou.")
