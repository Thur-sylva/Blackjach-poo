from view.view import View
from model.jogador import Jogador
from model.carta import Carta
from model.naipe import Naipe

v = View()
j = Jogador("Arthur")
j.mao.adicionar_carta(Carta("5", 5, Naipe.COPAS))
j.mao.adicionar_carta(Carta("K", 10, Naipe.ESPADAS))

v.exibir_mensagem("Bem vindo ao Blackjack!")  
v.exibir_mao(j)                               
v.exibir_pontuacao(j)                         
v.exibir_resultado("vitoria")                 