import random
import sys

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# 0 -> pedra
# 1 -> papel
# 2 -> tesoura

imagem = [pedra, papel, tesoura]

escolha_usuario = int(input("O que você escolhe? 0 para PEDRA, 1 para PAPEL e 2 para TESOURA: "))

if escolha_usuario < 0 or escolha_usuario > 2:
  print("Escolha inválida.")
  sys.exit()

print(imagem[escolha_usuario])

escolha_pc = random.randint(0, 2)
print("O computador escolhe: ")
print(imagem[escolha_pc])

if escolha_usuario == escolha_pc:
    print("Empate")
elif (escolha_usuario == 0 and escolha_pc == 2) or \
     (escolha_usuario == 1 and escolha_pc == 0) or \
     (escolha_usuario == 2 and escolha_pc == 1):
    print("Você ganhou")
else:
    print("Você perdeu")
