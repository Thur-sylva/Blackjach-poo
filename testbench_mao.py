from model.mao import Mao
from model.carta import Carta
from model.as_carta import As
from model.naipe import Naipe

m = Mao()
m.adicionar_carta(Carta("5", 5, Naipe.COPAS))
m.adicionar_carta(Carta("K", 10, Naipe.ESPADAS))

print(m)                      
print(m.calcular_pontuacao()) 
print(m.is_bust())            
print(m.is_blackjack())       

m2 = Mao()
m2.adicionar_carta(As(Naipe.COPAS))
m2.adicionar_carta(Carta("10", 10, Naipe.OUROS))
print(m2.calcular_pontuacao()) 
print(m2.is_blackjack())       