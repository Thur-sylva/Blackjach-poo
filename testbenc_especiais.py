from model.carta_especial import Carta_especial
from model.naipe import Naipe


k = Carta_especial("K", Naipe.ESPADAS)
print(k)
print(k.get_valor())

j = Carta_especial("J",Naipe.OUROS)
print(j)
print(j.get_valor())