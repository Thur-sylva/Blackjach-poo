from model.carta import Carta
from model.carta_especial import Carta_especial
from model.as_carta import As
from model.naipe import Naipe
import random

class Baralho:
    def __init__(self):
        self.cartas= self._criar_cartas()
    
    def _criar_cartas(self):
        cartas = []
        normais = ["2","3","4","5","6","7","8","9","10"]
        especiais = ["J", "Q", "K"]

        for naipe in Naipe:
            for simbolo in normais:
                valor = int(simbolo)
                cartas.append(Carta(simbolo, int(valor), naipe))

            for simbolo in especiais:
                cartas.append(Carta_especial(simbolo, naipe))

    
            cartas.append(As(naipe))

        return cartas
            

    def embaralhar(self):
        random.shuffle(self.cartas)

    def puxar_carta(self):
        return self.cartas.pop(0)
        
