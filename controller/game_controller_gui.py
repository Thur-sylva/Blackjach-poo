from model.baralho import Baralho
from model.jogador import Jogador
from model.dealer import Dealer
from model.repositorio import Repositorio
from view.view_gui import ViewGui


class GameControllerGui:
    def __init__(self):
        self.baralho      = Baralho()
        self.dealer       = Dealer("Dealer")
        self.jogador      = None
        self.repositorio  = Repositorio()
        self.rodada_ativa = False  
        self.view         = ViewGui()

        self.view.definir_callback_nome(self.iniciar_jogo)
        self.view.definir_callbacks(
            ao_clicar_hit=self.ao_clicar_hit,
            ao_clicar_stand=self.ao_clicar_stand,
            ao_clicar_novamente=self.nova_rodada
        )

    def iniciar_jogo(self, nome):
        self.jogador = Jogador(nome)
        self.view.janela.after(100, self._iniciar_rodada)

    def _iniciar_rodada(self):
        self.rodada_ativa = True  
        self.baralho = Baralho()
        self.baralho.embaralhar()
        if self.jogador:
            self.jogador.mao.cartas = []
        self.dealer.mao.cartas = []

        self.dealer.deal_card(self.jogador.mao, self.baralho)
        self.dealer.deal_card(self.jogador.mao, self.baralho)
        self.dealer.deal_card(self.dealer.mao, self.baralho)
        self.dealer.deal_card(self.dealer.mao, self.baralho)

        self.view.atualizar_mao_jogador(
            self.jogador.mao,
            self.jogador.mao.calcular_pontuacao(),
            nome=self.jogador.nome
        )
        self.view.atualizar_mao_dealer(self.dealer.mao, oculto=True)

        
        if self.jogador.mao.is_blackjack():
            self.rodada_ativa = False
            self.view.desabilitar_botoes()
            self.view.atualizar_mao_dealer(self.dealer.mao, oculto=False)
            self.view.janela.after(1200, lambda: self._finalizar("vitoria"))
        elif self.dealer.mao.is_blackjack():
            self.rodada_ativa = False
            self.view.desabilitar_botoes()
            self.view.atualizar_mao_dealer(self.dealer.mao, oculto=False)
            self.view.janela.after(1200, lambda: self._finalizar("derrota"))

    def ao_clicar_hit(self):
        if not self.rodada_ativa:  
            return
        self.dealer.deal_card(self.jogador.mao, self.baralho)
        self.view.atualizar_mao_jogador(
            self.jogador.mao,
            self.jogador.mao.calcular_pontuacao(),
            nome=self.jogador.nome
        )
        if self.jogador.mao.is_bust():
            self.rodada_ativa = False  
            self.view.desabilitar_botoes()
            self.view.atualizar_mao_dealer(self.dealer.mao, oculto=False)
            
            self.view.janela.after(1200, lambda: self._finalizar("derrota"))

    def ao_clicar_stand(self):
        if not self.rodada_ativa:  
            return
        self.rodada_ativa = False 
        self.view.desabilitar_botoes()
        self.view.atualizar_mao_dealer(self.dealer.mao, oculto=False)
       
        self.view.janela.after(700, self._dealer_joga_passo)

    def _dealer_joga_passo(self):
        
        if self.dealer.jogar():
            self.dealer.deal_card(self.dealer.mao, self.baralho)
            self.view.atualizar_mao_dealer(self.dealer.mao, oculto=False)
            self.view.janela.after(700, self._dealer_joga_passo)
        else:
            resultado = self._calcular_resultado()
            self.view.janela.after(700, lambda: self._finalizar(resultado))

    def _calcular_resultado(self):
        pont_jogador = self.jogador.mao.calcular_pontuacao()
        pont_dealer  = self.dealer.mao.calcular_pontuacao()

        if self.dealer.mao.is_bust():
            return "vitoria"
        elif pont_jogador > pont_dealer:
            return "vitoria"
        elif pont_dealer > pont_jogador:
            return "derrota"
        else:
            return "empate"

    def _finalizar(self, resultado):
        pont_jogador = self.jogador.mao.calcular_pontuacao()
        pont_dealer  = self.dealer.mao.calcular_pontuacao()

        self.repositorio.salvar_partida(
            self.jogador.nome, pont_jogador, pont_dealer, resultado
        )
        self.view.tela_resultado(resultado, pont_jogador, pont_dealer)

    def nova_rodada(self):
        self.view.janela.after(100, self._iniciar_rodada)

    def jogar(self):
        self.view.iniciar()