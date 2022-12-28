"""
COUNT - Itertools
"""
from itertools import count

contador = count()

print(next(contador))

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-

from itertools import count

contador = count(start=9, step=-1)
for valor in contador:
    print(round(valor, 2))

    if valor >= 10 or valor <= -10:
        break

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-

from itertools import count

contador = count()
lista = [
    'Otavio', 
    'Luis', 
    'Maria',
    ]
lista = zip(contador, lista)
print(list(lista))