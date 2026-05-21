from model.mao import Mao 
from abc import ABC, abstractmethod

class Participantes(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.mao = Mao()

    @abstractmethod
    def jogar(self):
        pass


    def revelar_mao(self):
        print (f"{self.nome}: {self.mao}")
    
        