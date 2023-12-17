from replit import clear
import arte

apostadores = {}

def adicionar_apostador(nome, oferta):
    apostadores[nome] = oferta

def ganhador(apostadores):
    maior = 0
    for pessoa in apostadores:
        if apostadores[pessoa] > maior: # comparando o valor
            ganhador = pessoa
            maior = apostadores[pessoa]

    print(f"O ganhador é {ganhador} com uma aposta de R${round(apostadores[ganhador], 2)}")

print(arte.logo)

continuar = True
while continuar:
    nome = input("Qual o seu nome? ")
    oferta = float(input("Qual a sua aposta? R$"))
    adicionar_apostador(nome, oferta)

    opcao_errada = True
    while opcao_errada == True:
        opcao = input("Tem mais alguém pra apostar? 'sim' ou 'nao': \n")
        if opcao == "nao":
            clear()
            continuar = False
            opcao_errada = False
        elif opcao == "sim":
            clear()
            opcao_errada = False
        else:
            print("Opção inválida.")

ganhador(apostadores)
