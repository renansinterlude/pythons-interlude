import random
import turtle

import colorgram
from turtle import Turtle, Screen
turtle.colormode(255)

lista_cores = [(31, 13, 5), (15, 47, 65), (152, 18, 77), (66, 13, 37), (254, 214, 143), (28, 107, 121), (243, 198, 128), (124, 63, 101), (219, 166, 111), (16, 32, 29), (16, 87, 97), (216, 55, 120), (54, 54, 85), (128, 93, 58), (42, 101, 99), (31, 83, 80), (164, 130, 81), (250, 171, 143), (92, 65, 25), (188, 102, 83)]

# caracteristicas da Clem
clementine = Turtle()
clementine.ht()
clementine.speed(0)
screen = Screen()
clementine.color("red")

# colocando clementine no canto da tela
clementine.pu()


def desenhar_circulo():
    clementine.begin_fill()
    clementine.circle(20)
    clementine.end_fill()


def desenhar_forma(lados):
    clementine.begin_fill()
    angulo = 360 / lados
    for _ in range(lados):
        clementine.forward(120/lados)  # vai deixar todos os lados com proporção igual de acordo com número de lados
        clementine.left(angulo)
    clementine.end_fill()

formas = [4, 5, 7, 8]

y = -300

for i in range(10):
    x = -350
    clementine.goto(x, y)
    for j in range(10):
        escolha = random.randint(1,2)
        clementine.color(random.choice(lista_cores))
        if escolha == 1:
            desenhar_circulo()
            # clementine.dot(30, random.choice(lista_cores))
        else:
            desenhar_forma(random.choice(formas))
        x += 70
        clementine.goto(x, y)
    y += 70


screen.exitonclick()