from model.participante import Participantes

class Jogador(Participantes):
    def __init__(self, nome):      
        super().__init__(nome)     

    def jogar(self, decisao):
        if decisao == "hit":
            return "hit"
        else:
            return "stand"