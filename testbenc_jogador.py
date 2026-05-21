
from model.jogador import Jogador
from model.carta import Carta
from model.naipe import Naipe

j = Jogador("Arthur")

j.mao.adicionar_carta(Carta("6",6,Naipe.OUROS))
j.mao.adicionar_carta(Carta("10",10,Naipe.COPAS))

j.revelar_mao()

print(j.mao.calcular_pontuacao)
print(j.jogar("hit"))
print(j.jogar("stand"))