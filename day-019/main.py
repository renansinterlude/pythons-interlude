import random
from turtle import Turtle, Screen


corrida_acontecendo = False
screen = Screen()
screen.setup(width=500, height=400)
aposta = screen.textinput("Aposta", "Quem vai ganhar a corrida? Escolha uma cor: ").lower()

cores = ["red", "orange", "yellow", "green", "blue", "purple"]
random.shuffle(cores)
cores_em_portugues = {"red": "vermelha",
                      "orange": "laranja",
                      "yellow": "amarela",
                      "green": "verde",
                      "blue": "azul",
                      "purple": "roxa"}

tartarugas = []
y = -100
for cor in cores:
    nova_tartaruga = Turtle(shape="turtle")
    nova_tartaruga.color(cor)
    nova_tartaruga.penup()
    nova_tartaruga.goto(x=-230, y=y)
    y += 40
    tartarugas.append(nova_tartaruga)

if aposta:
    corrida_acontecendo = True

while corrida_acontecendo:
    for tartaruga in tartarugas:
        if tartaruga.xcor() > 230:
            corrida_acontecendo = False
            ganhador = tartaruga.pencolor() # esse pencolor é a cor da tartaruga. tem que ser isso e não color diretamente porque o color retorna o pencolor e o fillcolor
            cor = cores_em_portugues[ganhador]  # pegando a chave do ganhador em ingles e alterando pro valor correspondente no dicionário cores_em_portugues
            if ganhador == aposta:
                print(f"Você ganhou! A tartaruga {cor} ganhou a corrida.")
            else:
                print(f"Você perdeu. A tartaruga {cor} ganhou a corrida.")
            break

        distancia = random.randint(0, 10)
        tartaruga.forward(distancia)


screen.exitonclick()
