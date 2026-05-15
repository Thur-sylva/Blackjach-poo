from model.baralho import Baralho

b =Baralho()

print(len(b.cartas))

b.embaralhar()
carta = b.puxar_carta()
print(carta)        

print(len(b.cartas))