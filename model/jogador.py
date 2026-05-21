from model.participante import Participantes


class Jogador(Participantes):
    def __iit__(self, nome, mao):
        super().__init__(nome, mao)

    def jogar(self, decisao):
        if decisao == "hit":
            return "hit"
        else:
            return "stand"

