from game_data import dados
from arte import logo, vs
import random
import os


#escolher 2 índices aleatórios da lista de dados
def escolha():
    escolha = random.randint(0, 49)
    return escolha


# pegando o número de seguidores de cada dado
def seguidores(dados, escolha):
    seguidores = dados[escolha]["seguidores"]
    return seguidores


def jogo():

    pontos = 0
    acerto = True
    escolha1 = escolha(
    )  # define a primeira posição antes do looping pra não trocar toda vez que o uusário acertar
    # dessa forma, a única escolha que muda é a 2 durante o funcionamento das partidas

    while acerto == True:  # partida
        # Imprimindo a logo
        print(logo)

        #Imprimindo pontuação abaixo do logo do jogo
        if pontos > 0:
            print(f"Acertou! Pontuação: {pontos} 🎉")
        else:
            print(f"Pontuação: {pontos}")

        # Escolhendo dado pra escolha2
        escolha2 = escolha()

        # Impedindo que números venham iguais
        while escolha1 == escolha2:
            escolha2 = escolha()

        # Pegando o numero de seguidores deles
        seguidores1 = seguidores(dados, escolha1)
        seguidores2 = seguidores(dados, escolha2)
        # print(seguidores1)
        # print(seguidores2)

        print(
            f"Compare A: {dados[escolha1]['nome']}, {dados[escolha1]['descricao']} de {dados[escolha1]['pais']}"
        )

        # Imprimindo o VS
        print(vs)

        print(
            f"Contra B: {dados[escolha2]['nome']}, {dados[escolha2]['descricao']} de {dados[escolha1]['pais']}"
        )

        # Perguntar qual tem mais
        aposta = input("Quem tem mais seguidores? Digite 'A' ou 'B': ").lower()

        # A e B são na vdd escolha1 e escolha2
        # comparar o numero de seguidores deles
        if seguidores1 > seguidores2:
            maior = 'a'
        else:
            maior = 'b'

        # Se acertou, limpar tela e começar de novo, marcando um ponto
        if aposta == maior:
            pontos += 1
            escolha1 = escolha2  # bota a segunda opção pra ser a primeira
            os.system("clear||cls")  # sai do if e começa partida de novo
        else:
            print(f"Errou! Pontuação final: {pontos} 😕")
            acerto = False  # saindo do looping da partida


# Looping. Depois de cada jogo, vem a pergunta. Se o usuário escolher algo além de S, ele sai do while e o programa para
jogar_de_novo = True
while jogar_de_novo == True:
    jogo()
    opcao = input("Quer jogar de novo? 'S' ou 'N': ").lower()
    if opcao == 's':
        os.system("clear||cls")
    else:
        jogar_de_novo = False