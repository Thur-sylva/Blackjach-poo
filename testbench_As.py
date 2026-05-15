from model.as_carta import As   
from model.naipe import Naipe 

a = As(Naipe.COPAS)

print(a)
print(a.get_valor(5))
print(a.get_valor(15))
