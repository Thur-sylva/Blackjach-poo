import tkinter as tk

BG_MESA      = "#1a5c38"
BG_ESCURO    = "#0f3d26"
BG_BOTAO_HIT = "#27ae60"
BG_BOTAO_STA = "#c0392b"
BG_TELA_INI  = "#0f3d26"
COR_TEXTO    = "#f0e6c8"
COR_DESTAQUE = "#f0c040"


class ViewGui:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Blackjack")
        self.janela.geometry("820x640")
        self.janela.resizable(False, False)
        self.janela.configure(bg=BG_TELA_INI)
        self.frame_atual = None
        self._ao_iniciar        = None
        self._ao_clicar_hit     = None
        self._ao_clicar_stand   = None
        self._ao_clicar_novamente = None
        self.tela_inicial()

    # ─────────────────────────────────────────
    # INFRAESTRUTURA
    # ─────────────────────────────────────────

    def trocar_tela(self, novo_frame):
        if self.frame_atual:
            self.frame_atual.destroy()
        self.frame_atual = novo_frame
        self.frame_atual.pack(expand=True, fill="both")

    def iniciar(self):
        self.janela.mainloop()

    def definir_callback_nome(self, ao_iniciar):
        self._ao_iniciar = ao_iniciar

    def definir_callbacks(self, ao_clicar_hit, ao_clicar_stand, ao_clicar_novamente):
        self._ao_clicar_hit       = ao_clicar_hit
        self._ao_clicar_stand     = ao_clicar_stand
        self._ao_clicar_novamente = ao_clicar_novamente

    # ─────────────────────────────────────────
    # TELA 1 — BOAS VINDAS
    # ─────────────────────────────────────────

    def tela_inicial(self):
        frame = tk.Frame(self.janela, bg=BG_TELA_INI)

        tk.Label(frame, text="♠  BLACKJACK  ♥", bg=BG_TELA_INI,
                 fg=COR_DESTAQUE, font=("Georgia", 52, "bold")).pack(pady=50)

        tk.Label(frame, text="Digite seu nome:", bg=BG_TELA_INI,
                 fg=COR_TEXTO, font=("Arial", 16)).pack(pady=8)

        self.entrada_nome = tk.Entry(frame, font=("Arial", 18),
                                     justify="center", width=20,
                                     bg="#f0e6c8", fg="#0f3d26",
                                     relief="flat", bd=6)
        self.entrada_nome.pack(pady=8)
        self.entrada_nome.bind("<Return>", lambda e: self._ao_clicar_jogar())

        tk.Button(frame, text="JOGAR", font=("Arial", 16, "bold"),
                  bg=BG_BOTAO_HIT, fg="white", width=14,
                  relief="flat", cursor="hand2",
                  command=self._ao_clicar_jogar).pack(pady=24)

        self.trocar_tela(frame)

    def _ao_clicar_jogar(self):
        nome = self.entrada_nome.get().strip()
        if not nome:
            return
        if self._ao_iniciar:
            self._ao_iniciar(nome)
        self.tela_jogo()

    # ─────────────────────────────────────────
    # TELA 2 — JOGO (MESA)
    # ─────────────────────────────────────────

    def tela_jogo(self):
        frame = tk.Frame(self.janela, bg=BG_MESA)

        # ── área dealer ──
        tk.Label(frame, text="D  E  A  L  E  R", bg=BG_MESA,
                 fg=COR_TEXTO, font=("Arial", 11, "bold")).pack(pady=(18, 4))

        self.canvas_dealer = tk.Canvas(frame, bg=BG_MESA,
                                       height=110, width=780,
                                       highlightthickness=0)
        self.canvas_dealer.pack()

        self.label_pont_dealer = tk.Label(frame, text="",
                                          bg=BG_MESA, fg=COR_TEXTO,
                                          font=("Arial", 11))
        self.label_pont_dealer.pack(pady=2)

        # ── separador ──
        tk.Frame(frame, bg=BG_ESCURO, height=3).pack(fill="x", padx=30, pady=8)

        # ── área jogador ──
        self.label_nome_jogador = tk.Label(frame, text="VOCÊ",
                                           bg=BG_MESA, fg=COR_TEXTO,
                                           font=("Arial", 11, "bold"))
        self.label_nome_jogador.pack(pady=(4, 4))

        self.canvas_jogador = tk.Canvas(frame, bg=BG_MESA,
                                        height=110, width=780,
                                        highlightthickness=0)
        self.canvas_jogador.pack()

        self.texto_pontuacao = tk.StringVar()
        self.texto_pontuacao.set("Pontuação: 0")
        tk.Label(frame, textvariable=self.texto_pontuacao,
                 bg=BG_MESA, fg=COR_DESTAQUE,
                 font=("Arial", 13, "bold")).pack(pady=4)

        # ── botões ──
        frame_botoes = tk.Frame(frame, bg=BG_MESA)
        frame_botoes.pack(pady=14)

        self.btn_hit = tk.Button(frame_botoes, text="HIT",
                                 font=("Arial", 15, "bold"),
                                 bg=BG_BOTAO_HIT, fg="white",
                                 width=10, relief="flat", cursor="hand2",
                                 command=self._hit)
        self.btn_hit.pack(side="left", padx=20)

        self.btn_stand = tk.Button(frame_botoes, text="STAND",
                                   font=("Arial", 15, "bold"),
                                   bg=BG_BOTAO_STA, fg="white",
                                   width=10, relief="flat", cursor="hand2",
                                   command=self._stand)
        self.btn_stand.pack(side="left", padx=20)

        self.trocar_tela(frame)

    def _hit(self):
        if self._ao_clicar_hit:
            self._ao_clicar_hit()

    def _stand(self):
        if self._ao_clicar_stand:
            self._ao_clicar_stand()

    # ─────────────────────────────────────────
    # DESENHO DE CARTAS NO CANVAS
    # ─────────────────────────────────────────

    def _desenhar_carta(self, canvas, x, y, simbolo, naipe_valor):
        cor = "#c0392b" if naipe_valor in ["♥️", "♦️", "♥", "♦"] else "#1a1a1a"
        canvas.create_rectangle(x, y, x+62, y+94,
                                 fill="white", outline="#aaaaaa", width=1)
        canvas.create_text(x+10, y+14, text=simbolo,
                           fill=cor, font=("Arial", 11, "bold"), anchor="center")
        canvas.create_text(x+31, y+47, text=naipe_valor,
                           fill=cor, font=("Arial", 20, "bold"), anchor="center")
        canvas.create_text(x+52, y+80, text=simbolo,
                           fill=cor, font=("Arial", 11, "bold"), anchor="center")

    def _desenhar_carta_oculta(self, canvas, x, y):
        canvas.create_rectangle(x, y, x+62, y+94,
                                 fill="#1a3a8f", outline="#aaaaaa", width=1)
        canvas.create_text(x+31, y+47, text="?",
                           fill="white", font=("Arial", 26, "bold"), anchor="center")

    # ─────────────────────────────────────────
    # ATUALIZAR TELA DO JOGO
    # ─────────────────────────────────────────

    def atualizar_mao_jogador(self, mao, pontuacao, nome="VOCÊ"):
        self.label_nome_jogador.config(text=nome.upper())
        self.canvas_jogador.delete("all")
        x = 20
        for carta in mao.cartas:
            self._desenhar_carta(self.canvas_jogador, x, 8,
                                 carta.simbolo, carta.naipe.value)
            x += 72
        self.texto_pontuacao.set(f"Pontuação: {pontuacao}")

    def atualizar_mao_dealer(self, mao, oculto=False):
        self.canvas_dealer.delete("all")
        self.label_pont_dealer.config(text="")
        if oculto:
            if mao.cartas:
                self._desenhar_carta_oculta(self.canvas_dealer, 20, 8)
            if len(mao.cartas) > 1:
                c = mao.cartas[1]
                self._desenhar_carta(self.canvas_dealer, 92, 8,
                                     c.simbolo, c.naipe.value)
            return
        x = 20
        for carta in mao.cartas:
            self._desenhar_carta(self.canvas_dealer, x, 8,
                                 carta.simbolo, carta.naipe.value)
            x += 72
        pont = sum(c.get_valor() for c in mao.cartas)
        self.label_pont_dealer.config(text=f"Dealer: {mao.calcular_pontuacao()} pts")

    def desabilitar_botoes(self):
        if hasattr(self, "btn_hit"):
            self.btn_hit.config(state="disabled")
            self.btn_stand.config(state="disabled")

    # ─────────────────────────────────────────
    # TELA 3 — RESULTADO
    # ─────────────────────────────────────────

    def tela_resultado(self, resultado, pont_jogador, pont_dealer):
        frame = tk.Frame(self.janela, bg=BG_MESA)

        if resultado == "vitoria":
            mensagem = "🎉  VOCÊ GANHOU!  🎉"
            cor = COR_DESTAQUE
        elif resultado == "derrota":
            mensagem = "💀  VOCÊ PERDEU!"
            cor = "#e74c3c"
        else:
            mensagem = "🤝  EMPATE!"
            cor = COR_TEXTO

        tk.Label(frame, text=mensagem, bg=BG_MESA,
                 fg=cor, font=("Georgia", 34, "bold")).pack(pady=60)

        tk.Label(frame, text=f"Sua pontuação:  {pont_jogador}",
                 bg=BG_MESA, fg=COR_TEXTO,
                 font=("Arial", 16)).pack(pady=6)

        tk.Label(frame, text=f"Dealer:  {pont_dealer}",
                 bg=BG_MESA, fg=COR_TEXTO,
                 font=("Arial", 16)).pack(pady=6)

        tk.Frame(frame, bg=BG_ESCURO, height=2).pack(fill="x", padx=60, pady=20)

        tk.Button(frame, text="JOGAR NOVAMENTE",
                  font=("Arial", 14, "bold"),
                  bg=BG_BOTAO_HIT, fg="white",
                  width=18, relief="flat", cursor="hand2",
                  command=self._novamente).pack(pady=10)

        tk.Button(frame, text="SAIR",
                  font=("Arial", 12),
                  bg=BG_ESCURO, fg=COR_TEXTO,
                  width=10, relief="flat", cursor="hand2",
                  command=self.janela.destroy).pack(pady=6)

        self.trocar_tela(frame)

    def _novamente(self):
        if self._ao_clicar_novamente:
            self._ao_clicar_novamente()
        self.tela_jogo()

    