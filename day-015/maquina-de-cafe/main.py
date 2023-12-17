import sys

MENU = {
    "espresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
            "leite": 0
        },
        "preco": 1.5,
    },
    "latte": {
        "ingredientes": {
            "agua": 200,
            "leite": 150,
            "cafe": 24,
        },
        "preco": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "agua": 250,
            "leite": 100,
            "cafe": 24,
        },
        "preco": 3.0,
    }
}

recursos = {
    "agua": 300,
    "leite": 200,
    "cafe": 100,
    "reserva": 0
}


def verifica_recursos(escolha):
    if MENU[escolha]["ingredientes"]["agua"] > recursos["agua"]:
        print("Desculpe, falta água 💦")
        return False
    elif MENU[escolha]["ingredientes"]["leite"] > recursos["leite"]:
        print("Desculpe, falta leite 🥛")
        return False
    elif MENU[escolha]["ingredientes"]["cafe"] > recursos["cafe"]:
        print("Desculpe, falta café ☕")
        return False
    else:
        return True


def pagamento():
    """Retorna o valor das moedas inseridas."""
    print("Insira as moedas: ")
    valor_pago = 0
    valor_pago = int(input("Quantas moedas de 25 centavos? ")) * 0.25
    valor_pago += int(input("Quantas moedas de 10 centavos? ")) * 0.1
    valor_pago += int(input("Quantas moedas de 5 centavos? ")) * 0.05
    valor_pago += int(input("Quantas moedas de 1 centavo? ")) * 0.01
    return valor_pago


def adiciona_fundos(preco_cafe):
    recursos["reserva"] += preco_cafe


def troco(valor_pago, preco_cafe):
    troco = 0
    if valor_pago > preco_cafe:
        troco = valor_pago - preco_cafe
        print(f"Aqui está seu troco de R${round(troco, 2)}")


def verifica_pagamento(valor_pago, preco_cafe):
    """Retorna True se o usuário inseriu dinheiro suficiente e False se não."""
    if valor_pago >= preco_cafe:
        return True
    else:
        return False


def subtrai_recursos(escolha):
    recursos["agua"] -= MENU[escolha]["ingredientes"]["agua"]
    recursos["leite"] -= MENU[escolha]["ingredientes"]["leite"]
    recursos["cafe"] -= MENU[escolha]["ingredientes"]["cafe"]


def imprimir_recursos():
    print(f"💦 Água: {recursos['agua']}")
    print(f"🥛 Leite: {recursos['leite']}")
    print(f"☕ Café: {recursos['cafe']}")
    print(f"💵 Dinheiro: {recursos['reserva']}")


def iniciar():

    continuar = True
    while continuar:

        escolha = ''
        while escolha != 'espresso' and escolha != 'latte' and escolha != 'cappuccino':
            escolha = input("O que você vai querer? (espresso/latte/cappuccino): ").lower()

            if escolha == "off":
                sys.exit()

            if escolha == 'recursos':
                imprimir_recursos()

        preco_cafe = MENU[escolha]["preco"]

        fazer_cafe = verifica_recursos(escolha)
        if fazer_cafe:
            valor_pago = pagamento()
            if verifica_pagamento(valor_pago, preco_cafe):
                subtrai_recursos(escolha)
                adiciona_fundos(preco_cafe)
                troco(valor_pago, preco_cafe)
                print(f"Aqui está o seu {escolha} ☕. Aproveite!")
            else:
                print("Desculpe, não é o suficiente. Você será reembolsado.")


iniciar()