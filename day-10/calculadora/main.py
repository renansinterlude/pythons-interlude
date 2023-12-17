import sys
# adição
def adicionar(n1, n2):
    return n1 + n2

# subtração
def subtrair(n1, n2):
    return n1 - n2

# multiplicação
def multiplicar(n1, n2):
    return n1 * n2

# divisão
def dividir(n1, n2):
    return n1 / n2

operacoes = {
    "+": adicionar,
    "-": subtrair,
    "*": multiplicar,
    "/": dividir
}

def calcular(n1, n2, operacao): # passei a operação como parâmetro só para não parecer que saiu do nada.
    funcao = operacoes[operacao]
    resposta = funcao(n1, n2)
    return resposta

def calculadora():
    n1 = float(input("Qual o primeiro número? ")) # pede o n1 apenas uma vez.
    for operacao in operacoes:
        print(operacao)
    
    continuar = True
    while continuar:
        operacao = input("Escolha a operação: ")
        n2 = float(input("Qual o próximo número? "))
        
        resposta = calcular(n1, n2, operacao)   # 1ª vez: cálculo de primeiro n1 com n2. 
                                                # 2ª vez: calculo de novo n1 com n2 
        print(f"{n1} {operacao} {n2} = {resposta}")
        
        invalido = True
        while invalido:
            continuar = input(f"Quer fazer mais alguma conta com o {resposta}?\n's' para continuar, 'n' para começar com novos números ou 't' para sair da calculadora: ")
            if continuar == "s":
                n1 = resposta # se sim, n1 se torna a resposta anterior. 
                              # Assim, é possível reutilizá-la como base nas próximas contas
                invalido = False
            elif continuar == "n":
                invalido = False
                continuar = False # sai do loop
                calculadora()  # inicia a função calculadora de novo, 
                               # setando o continuar pra True e iniciando um novo loop
            elif continuar == "t":
                sys.exit()
            else:
                print("Opção não existe.")

calculadora()


# funcao = operacoes["*"]
# funcao(2, 3)
# isso vai fazer com que a funcao seja substituida com o nome da operação e da função ao mesmo tempo, tornando uma função
