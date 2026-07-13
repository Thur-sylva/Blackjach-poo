from unittest import result

from model.baralho import Baralho
from model.jogador import Jogador
from model.dealer import Dealer
from view.view import View
from model.repositorio import Repositorio

class GameController:
    def __init__(self):
        self.baralho = Baralho()
        self.view    = View()
        self.repositorio = Repositorio()
        nome = self.view.pedir_nome()
        self.jogador = Jogador(nome)
        self.dealer  = Dealer("Dealer")
        

    def iniciar(self):
        self.baralho.embaralhar()
        self.dealer.deal_card(self.jogador.mao, self.baralho)
        self.dealer.deal_card(self.jogador.mao, self.baralho)
        self.dealer.deal_card(self.dealer.mao, self.baralho)
        self.dealer.deal_card(self.dealer.mao, self.baralho)

    def turno_jogador(self):
        while True:
            self.view.exibir_mao(self.jogador)
            decisao = self.view.pedir_decisao()
            if decisao == "hit":
                self.dealer.deal_card(self.jogador.mao, self.baralho)
                self.view.exibir_mao(self.jogador)
                if self.jogador.mao.is_bust():
                    self.view.exibir_mensagem("Você estourou! Bust!")
                    return True
            else:
                return False

    def turno_dealer(self):
        while self.dealer.jogar():
            self.dealer.deal_card(self.dealer.mao, self.baralho)

    def determinar_vencedor(self):
        pont_jogador = self.jogador.mao.calcular_pontuacao()
        pont_dealer  = self.dealer.mao.calcular_pontuacao()

        if self.jogador.mao.is_bust():
            resultado = ("derrota")

        elif self.dealer.mao.is_bust():
            resultado = ("vitoria")

        elif pont_jogador > pont_dealer:
            resultado = ("vitoria")

        elif pont_dealer > pont_jogador:
            resultado = ("derrota")

        else:
            resultado = ("empate")

        self.repositorio.salvar_partida(
            self.jogador.nome,
            pont_jogador,
            pont_dealer,
            resultado)
        self.view.exibir_resultado(resultado)



    def resetar(self):
        self.baralho = Baralho()         
        self.jogador.mao.cartas = []    
        self.dealer.mao.cartas  = []    



    def jogar(self):
        self.view.exibir_mensagem("------ Bem vindo ao Blackjack! ------")

        while True: 
            self.resetar()
            self.iniciar()
            bust = self.turno_jogador()

            if not bust:
                self.turno_dealer()
                self.view.exibir_mao(self.dealer)
                self.view.exibir_pontuacao(self.dealer)
            self.determinar_vencedor()
            self.view.exibir_historico(self.repositorio.buscar_historico())

            if not self.view.pedir_continuar():  
                self.view.exibir_mensagem("Obrigado por jogar! Até logo!")
                break

    
   