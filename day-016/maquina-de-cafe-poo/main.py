import coffee_maker
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

caixa = MoneyMachine()
cafeteira = CoffeeMaker()

is_on = True
while is_on:
    escolha = ''
    # perguntando pro usuário qual café
    menu = Menu()
    opcoes = menu.get_items()
    while escolha not in ['latte', 'espresso', 'cappuccino', 'off', 'report']:
        escolha = input(f"O que você vai querer? ({opcoes}): ").lower()
    if escolha == 'off':
        is_on = False
    elif escolha == 'report':
        # printando recursos
        cafeteira.report()
        caixa.report()
    else:
        cafe = menu.find_drink(escolha)
        preco = cafe.cost
        if cafeteira.is_resource_sufficient(cafe):
            if caixa.make_payment(preco):
                cafeteira.make_coffee(cafe)