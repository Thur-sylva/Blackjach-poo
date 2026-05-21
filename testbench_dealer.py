
from model.dealer import Dealer
from model.jogador import Jogador
from model.baralho import Baralho


d = Dealer("roberto")
j= Jogador("Arthur")
b= Baralho()
b.embaralhar()


d.deal_card(j.mao, b)
d.deal_card(j.mao,b)

d.deal_card(d.mao,b)
d.deal_card(d.mao,b)

d.revelar_mao()
j.revelar_mao

print(d.mao.calcular_pontuacao())
print(d.jogar())
