from model.repositorio import Repositorio

r = Repositorio()
r.salvar_partida("Arthur", 18, 15, "vitoria")
r.salvar_partida("Arthur", 23, 19, "derrota")

historico = r.buscar_historico()
for partida in historico:
    print(partida)