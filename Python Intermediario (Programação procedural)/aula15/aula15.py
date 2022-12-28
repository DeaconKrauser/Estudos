'''
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos

'''
#METODOS DE COMBINAÇÃO

from itertools import combinations

pessoas = [
    'Luiz',
    'André',
    'Otavio',
    'Maria',
    'Pedro',
    ]

for grupo in combinations(pessoas, 2):
    print(grupo)

/*/*/*/*/*/*/*/*/*/*

from itertools import combinations

pessoas = [
    'Luiz',
    'André',
    'Otavio',
    'Maria',
    'Pedro',
    ]

for grupo in permutations(pessoas, 2):
    print(grupo)

/*/*/*/*/*/*/*/*/*/*

from itertools import combinations, permutations, product

pessoas = [
    'Luiz',
    'André',
    'Otavio',
    'Maria',
    'Pedro',
    ]

for grupo in product(pessoas, repeat=2):
    print(grupo)

