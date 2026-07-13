import tkinter as tk

class ViewGui:
    def __init__(self):
        self.janela = tk.Tk()                    
        self.janela.title("Blackjack")          
        self.janela.geometry("800x600")
        self.janela.configure(bg="#395adf")
        self.frame_atual = None
        self.tela_inicial()

    def trocar_tela(self, novo_frame):
        if self.frame_atual:
            self.frame_atual.destroy()
        self.frame_atual = novo_frame
        self.frame_atual.pack(expand=True, fill="both")

    def iniciar(self):
        self.janela.mainloop()

    def tela_inicial(self):
        frame = tk.Frame(self.janela, bg="#395adf")

        tk.Label(frame, text="Blackjack", bg="#395adf",
             fg="white", font=("Arial", 48, "bold")).pack(pady=40)

        tk.Label(frame, text="Digite seu nome:", bg="#395adf",
             fg="white", font=("Arial", 16)).pack(pady=10)

        self.entrada_nome = tk.Entry(frame, font=("Arial", 16))
        self.entrada_nome.pack(pady=10)

        tk.Button(frame, text="Jogar", font=("Arial", 16),
              command=self._ao_clicar_jogar).pack(pady=20)

        self.trocar_tela(frame)


    def _ao_clicar_jogar(self):
        nome = self.entrada_nome.get()  
        if nome.strip() == "":         
            return                     
        print(f"Nome digitado: {nome}") 
        self.tela_jogo()

    
    def tela_jogo(self):
        frame = tk.Frame(self.janela, bg="#395adf")

    
        tk.Label(frame, text="DEALER", bg="#395adf",
             fg="white", font=("Arial", 14, "bold")).pack(pady=10)

        self.texto_mao_dealer = tk.StringVar()
        self.texto_mao_dealer.set("? ?")  

        tk.Label(frame, textvariable=self.texto_mao_dealer,
             bg="#395adf", fg="white", font=("Arial", 20)).pack(pady=5)

   
        tk.Label(frame, text="─" * 40, bg="#395adf", fg="white").pack(pady=10)

    
        tk.Label(frame, text="VOCÊ", bg="#395adf",
             fg="white", font=("Arial", 14, "bold")).pack(pady=10)

        self.texto_mao_jogador = tk.StringVar()
        self.texto_mao_jogador.set("")
        tk.Label(frame, textvariable=self.texto_mao_jogador,
             bg="#395adf", fg="white", font=("Arial", 20)).pack(pady=5)

    
        self.texto_pontuacao = tk.StringVar()
        self.texto_pontuacao.set("Pontuação: 0")
        tk.Label(frame, textvariable=self.texto_pontuacao,
             bg="#395adf", fg="white", font=("Arial", 14)).pack(pady=5)

    
        frame_botoes = tk.Frame(frame, bg="#395adf")
        frame_botoes.pack(pady=20)

        tk.Button(frame_botoes, text="Hit", font=("Arial", 16),
              bg="green", fg="white",
              command=self._ao_clicar_hit).pack(side="left", padx=20)

        tk.Button(frame_botoes, text="Stand", font=("Arial", 16),
              bg="red", fg="white",
              command=self._ao_clicar_stand).pack(side="left", padx=20)

        self.trocar_tela(frame)

    
    def _ao_clicar_hit(self):
        print("hit clicado")

    def _ao_clicar_stand(self):
         self.tela_resultado("vitoria", 18, 15)
       

    def atualizar_mao_jogador(self, mao, pontuacao):
        self.texto_mao_jogador.set(str(mao))
        self.texto_pontuacao.set(f"Pontuação: {pontuacao}")

    def atualizar_mao_dealer(self, mao):
        self.texto_mao_dealer.set(str(mao))


    def tela_resultado(self, resultado, pont_jogador, pont_dealer):
        frame = tk.Frame(self.janela, bg="#395adf")

    
        if resultado == "vitoria":
            mensagem = "Você ganhou!!"
            cor = "yellow"
        elif resultado == "derrota":
            mensagem = "Você perdeu!"
            cor = "red"
        else:
            mensagem = "Empate!"
            cor = "white"

        tk.Label(frame, text=mensagem, bg="#395adf",
             fg=cor, font=("Arial", 36, "bold")).pack(pady=40)


        tk.Label(frame, text=f"Sua pontuação: {pont_jogador}",
             bg="#395adf", fg="white", font=("Arial", 16)).pack(pady=5)

        tk.Label(frame, text=f"Dealer: {pont_dealer}",
             bg="#395adf", fg="white", font=("Arial", 16)).pack(pady=5)

   
        tk.Button(frame, text="Jogar Novamente", font=("Arial", 16),
              bg="green", fg="white",
              command=self._ao_clicar_novamente).pack(pady=30)

        self.trocar_tela(frame)

    def _ao_clicar_novamente(self):
        print("jogar novamente clicado")
        self.tela_jogo()  

