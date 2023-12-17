from question_model import Pergunta
from data import *
from prettytable import PrettyTable
from quiz_brain import QuizBrain

tabela = PrettyTable()
tabela.add_column("Tema", ["Jogos",
                           "Pretty Little Liars ('PLL')",
                           "True Blood",
                           "The Walking Dead ('TWD')",
                           "Sly Cooper",
                           "Life is Strange ('LIS')"])

temas = {
    "pll": perguntas_pll,
    "jogos": perguntas_jogos,
    "true blood": perguntas_true_blood,
    "twd": perguntas_twd,
    "sly cooper": perguntas_sly_cooper,
    "truco": perguntas_truco,
    "lis": perguntas_life_is_strange
}

banco_perguntas = []

tema_perguntas = False
while not tema_perguntas:
    print(tabela)
    tipo_quiz = input("Qual o tema escolhido?: ").lower()
    tema_perguntas = temas.get(tipo_quiz)

for questao in tema_perguntas:
    texto = questao["pergunta"]
    resposta = questao["resposta_correta"]
    nova_pergunta = Pergunta(texto, resposta)
    banco_perguntas.append(nova_pergunta)

quiz = QuizBrain(banco_perguntas)

while quiz.ainda_tem_perguntas():
    quiz.proxima_pergunta()

print("Você completou o Quiz! 🥳")
print(f"Sua pontuação final foi {quiz.pontos}/{quiz.numero_pergunta} 🌟")  # dentro da classe
# quiz = self. Fora dela é quiz. mesmo.