from model.carta import Carta

class As(Carta):
    def __init__(self, naipe):
        super().__init__("A", 11, naipe)
    
    def get_valor(self, pontuacao_atual):
        if pontuacao_atual + 11 > 21:
            return 1
        else:
            return 11
    