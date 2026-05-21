
from model.as_carta import As


class Mao:
    def __init__(self):
        self.cartas =[]

    def adicionar_carta(self, carta):
        self.cartas.append(carta)

    def calcular_pontuacao(self):
        pontuacao = 0
        ases = []

        for carta in self.cartas:
            if isinstance(carta, As):
                ases.append(carta)
            else:
                pontuacao += carta.get_valor()

        for az in ases:
            pontuacao += az.get_valor(pontuacao)
        
        return pontuacao
    
    def is_bust(self):
       return self.calcular_pontuacao() > 21
        
        
    def is_blackjack(self):
        return len(self.cartas) == 2 and self.calcular_pontuacao() == 21

           
        

    def __str__(self):
        return " ".join(str(carta) for carta in self.cartas)
    
