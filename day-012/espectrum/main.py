import random
import sys
import replit

def jogar():
    # Perguntar a dificuldade. Se dificil, vidas = 5 | se fácil, vidas = 10
    dificuldade_invalida = True
    while dificuldade_invalida:
        dificuldade = input("Qual a dificuldade? 'facil' ou 'dificil': ")
        if dificuldade == 'facil':
            vidas = 10
            dificuldade_invalida = False
        elif dificuldade == 'dificil':
            vidas = 5
            dificuldade_invalida = False
        else:
            print("Dificuldade inválida.")
            dificuldade_invalida = True

    # Comparar com o número selecionado.
    def comparar(numero, palpite):
        if palpite > numero:
            print("📈 Muito alto. \n")
            # return False
        elif palpite < numero:
            print("📉 Muito baixo. \n")
            # return False
        else:
            print(f"🎉 Você acertou! O número era {numero}!")
            # return True

    def fim_de_jogo(numero, palpite):
        if numero == palpite:
            return True
        return False

    # Selecionar um número aleatório de 1 a 100
    numero = random.randint(1, 100)
    print("Estou pensando num número de 1 a 100...")

    # Perguntar um número pro usuário
    acertou = False
    while not acertou:
        if vidas > 0 and acertou == False:

            if vidas == 1:
                print(f"Você tem {vidas} vida restante.")
            else:
                print(f"Você tem {vidas} vidas restantes.")

            palpite = int(input("Adivinhe o número: "))
            vidas -= 1
            # acertou = comparar(numero, palpite) # seta acertou pra verdadeiro ou falso além de imprimir a situação
            comparar(numero, palpite)
            acertou = fim_de_jogo(numero, palpite)
        else:
            print("💔 Você perdeu.")
            acertou = True

    if input("Quer jogar de novo? 's' ou 'n': ") == 's':
        replit.clear()
        jogar()
    else:
        sys.exit() # funciona sem esse else também

jogar()