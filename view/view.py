
class View:


    def exibir_mensagem(self,msg):
        print(msg)


    def exibir_mao(self,participante):
        print(f"{participante.nome}:  {participante.mao}")

    def exibir_pontuacao(self, participante):
        print(f"{participante.nome}: {participante.mao.calcular_pontuacao()} pontos")

    def pedir_decisao(self):
        print("\n[1] Hit")
        print("\n[2] Stand")

        escolha = input("Digite a sua escolha: ")
        if escolha == "1":
            return "hit"
        else:
            return "stand"
        
    def exibir_resultado(self, resultado):
        if resultado == "vitoria":
            print("  ")
            print ("Você ganhou!!")
            print("  ")
        elif resultado == "derrota":
            print("  ")
            print ("Você perdeu")
            print("  ")
        else:
            print("  ")
            print("empate!")
            print("  ")

    def pedir_nome(self):
     nome = input("Digite o seu nome: ")
     return nome
    
    def pedir_continuar(self):
        escolha = input("\nDeseja jogar     novamente? [1] Sim  [2] Não: ")
        if escolha == "1":
            return True
        else:
            return False
    
    def exibir_historico(self, historico):
        print("\n------------Histórico de Partidas-----------------------------")

        if not historico:
            print("Nenhuma partida registrada")
            return
        for i, partida in enumerate(historico, 1):
            print(f"{i}. {partida['jogador']} | "
                  f"Você: {partida['pontuacao_jogador']} |"
                  f"Dealer: {partida['pontuacao_dealer']} | "
                  f"Resultado: {partida['resultado']}")

        print("---------------------------------------------------------------")
        
