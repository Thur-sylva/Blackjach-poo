from model.naipe import Naipe

class Carta:
    def __init__(self, simbolo, valor, naipe):
        self.simbolo = simbolo
        self.valor = valor
        self.naipe = naipe

    def get_valor(self):
        return self.valor
    
    def __str__(self):
        return self.simbolo + self.naipe.value 