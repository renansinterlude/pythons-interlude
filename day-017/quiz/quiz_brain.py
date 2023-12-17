class QuizBrain:
    def __init__(self, lista_pergunta):
        self.numero_pergunta = 0
        self.pontos = 0
        self.lista_pergunta = lista_pergunta

    def ainda_tem_perguntas(self):
        return self.numero_pergunta < len(self.lista_pergunta)  # tá pegando o numero_pergunta
        # do proxima_pergunta pq o outro que tem é do init e só serve para inicializar mesmo.
        # Tava em dúvida sobre como ele iria reconhecer qual dos dois numero_pergunta era para usar

    def proxima_pergunta(self):
        pergunta_atual = self.lista_pergunta[self.numero_pergunta]
        self.numero_pergunta += 1
        resposta = input(f"Q.{self.numero_pergunta}: {pergunta_atual.texto} (Verdadeiro/Falso)?: ")
        self.checar_resposta(resposta, pergunta_atual.resposta)

    def checar_resposta(self, resposta_usuario, resposta_certa):
        if resposta_usuario.lower() == resposta_certa.lower():
            print("🎉 Acertou! 🎉")
            self.pontos += 1
        else:
            print("❌ Errou! ❌")
        print(f"A resposta certa é: {resposta_certa}")
        print(f"Pontuação: {self.pontos}/{self.numero_pergunta}\n")