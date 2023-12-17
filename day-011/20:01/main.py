import random
import sys
import replit
from arte import logo

def jogar():
    def jogar_de_novo():
        jogar_mais_uma_vez = input("Você quer jogar uma partida de Blackjack? 's' ou 'n': ")
        if jogar_mais_uma_vez == 's':
            replit.clear()
            print(logo)
            jogar()
        else:
            sys.exit()

    def pegar_carta(cartas):
        return random.choice(cartas)

    def vencedor(placar_pc, placar_usuario):
        pontos_usuario = abs(placar_usuario - 21)
        pontos_pc = abs(placar_pc - 21)

        print(f"	Sua mão final: {cartas_usuario}, placar final: {placar_usuario}")
        print(f"	Mão final do computador: {cartas_pc}, placar final: {placar_pc}")

        tamanho_baralho_pc = len(cartas_pc)
        tamanho_baralho_usuario = len(cartas_usuario)

        if placar_usuario > 21:
            print("Você ultrapassou. Você perdeu. 😤\n")
        elif tamanho_baralho_pc == 2 and 10 in cartas_pc and 11 in cartas_pc:
            print("PC ganhou com um Blackjack! 💻👾\n") 
        elif tamanho_baralho_usuario == 2 and 10 in cartas_usuario and 11 in cartas_usuario:
            print("Você ganhou com um Blackjack! 🎇🧨\n")
        elif pontos_usuario < pontos_pc or placar_pc > 21:
            print("Você ganhou! 🥳\n")
        elif pontos_pc < pontos_usuario:
            print("Você perdeu. 😿\n")
        else:
            print("Empate.😿\n")

        jogar_de_novo()

    ##################### Inicialização das variáveis e mão inicial ########################

    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    cartas_pc = []
    cartas_usuario = []
    placar_pc = 0
    placar_usuario = 0

    while placar_pc < 17:
            cartas_pc.append(pegar_carta(cartas))
            placar_pc = sum(cartas_pc)

    def iniciar_mao_usuario():
        for carta in range(2):
            cartas_usuario.append(pegar_carta(cartas))

    iniciar_mao_usuario()

    def calcular_placar(cartas_pc, cartas_usuario):

        placar_usuario = sum(cartas_usuario)
        placar_pc = sum(cartas_pc)

        if 11 in cartas_pc:
            if placar_pc > 21:
                index_11 = cartas_pc.index(11)
                cartas_pc[index_11] = 1
                placar_pc = sum(cartas_pc)

        if 11 in cartas_usuario:
            if placar_usuario > 21:
                index_11 = cartas_usuario.index(11)
                cartas_usuario[index_11] = 1
                placar_usuario = sum(cartas_usuario)

        print(f"    Suas cartas: {cartas_usuario}, placar: {placar_usuario}")
        print(f"    1ª carta do PC: [{cartas_pc[0]}]")

        continuar = input("Deseja comprar uma carta? 's' ou 'n': ")
        if continuar == 's':
            print("\n")
            cartas_usuario.append(pegar_carta(cartas))
            calcular_placar(cartas_pc, cartas_usuario)
        else:
            print("\n") # Quebra de linha no resultado final
            vencedor(placar_pc, placar_usuario)

    calcular_placar(cartas_pc, cartas_usuario)

if input("Você quer jogar uma partida de Blackjack? 's' ou 'n': ") == 's':
    replit.clear()
    print(logo)
    jogar()
