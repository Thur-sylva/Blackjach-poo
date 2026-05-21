from model.participante import Participantes


class Dealer(Participantes):

    def jogar(self):
         if self.mao.calcular_pontuacao()<=17:
              return True
         else: 
              return False
         
    def deal_card(self,mao, baralho):
         carta = baralho.puxar_carta()
         mao.adicionar_carta(carta)
         
         
    
    