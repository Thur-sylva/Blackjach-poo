from model.baralho import Baralho
from model.jogador import Jogador
from model.dealer import Dealer
from view.view import View

class GameController:
    def __init__(self):
        self.baralho = Baralho()
        self.view    = View()
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
                if self.jogador.mao.is_bust():
                    self.view.exibir_mensagem("Você estourou! Bust!")
                    break
            else:
                break

    def turno_dealer(self):
        while self.dealer.jogar():
            self.dealer.deal_card(self.dealer.mao, self.baralho)

    def determinar_vencedor(self):
        pont_jogador = self.jogador.mao.calcular_pontuacao()
        pont_dealer  = self.dealer.mao.calcular_pontuacao()

        if self.jogador.mao.is_bust():
            self.view.exibir_resultado("derrota")
        elif self.dealer.mao.is_bust():
            self.view.exibir_resultado("vitoria")
        elif pont_jogador > pont_dealer:
            self.view.exibir_resultado("vitoria")
        elif pont_dealer > pont_jogador:
            self.view.exibir_resultado("derrota")
        else:
            self.view.exibir_resultado("empate")



    def resetar(self):
        self.baralho = Baralho()         
        self.jogador.mao.cartas = []    
        self.dealer.mao.cartas  = []    



    def jogar(self):
        self.view.exibir_mensagem("------ Bem vindo ao Blackjack! ------")

        while True: 
            self.resetar()
            self.iniciar()
            self.turno_jogador()
            self.turno_dealer()
            self.view.exibir_mao(self.dealer)
            self.view.exibir_pontuacao(self.dealer)
            self.determinar_vencedor()

            if not self.view.pedir_continuar():  
                self.view.exibir_mensagem("Obrigado por jogar! Até logo!")
                break

    
   