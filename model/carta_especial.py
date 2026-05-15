from model.carta import Carta

class Carta_especial(Carta):
    def __init__(self, simbolo, naipe):
        super().__init__(simbolo, 10, naipe)
            
