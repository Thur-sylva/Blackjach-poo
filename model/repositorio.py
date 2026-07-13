import json 
import os 

class Repositorio:
    def __init__(self):
        self.caminho = "data/historico.json"

    
    def _carregar(self):
        if not os.path.exists(self.caminho):
            return {"partidas": []}

        if os.path.getsize(self.caminho) == 0:
            return {"partidas": []}

        try:
            with open(self.caminho, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"partidas": []}

        
    def salvar_partida(self, jogador, pont_jogador, pont_dealer, resultado):
        dados = self._carregar()
        nova_partida = {
            "jogador": jogador,
            "pontuacao_jogador": pont_jogador,
            "pontuacao_dealer": pont_dealer,
            "resultado": resultado
        }

        dados["partidas"].append(nova_partida)

        os.makedirs("data", exist_ok=True)

        with open(self.caminho, "w") as f:
            json.dump(dados, f, indent=4)
    

    def buscar_historico(self):
        dados = self._carregar()
        return dados["partidas"]