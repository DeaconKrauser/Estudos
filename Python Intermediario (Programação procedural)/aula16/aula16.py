'''
Groupby - Agrupando valores do dicionario em py.
'''

from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Otavio', 'nota': 'C'},
    {'nome': 'Luis', 'nota': 'B'},
    {'nome': 'João', 'nota': 'D'},
    {'nome': 'Andre', 'nota': 'F'},
    {'nome': 'Mateus', 'nota': 'A'},
    {'nome': 'Maria', 'nota': 'A'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')
    for aluno in valores_agrupados:
        print(aluno)
    print()

/*/*/*/*/*/*/*/*/*/*/*/

# tee = Copia
from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Otavio', 'nota': 'C'},
    {'nome': 'Luis', 'nota': 'B'},
    {'nome': 'João', 'nota': 'D'},
    {'nome': 'Andre', 'nota': 'F'},
    {'nome': 'Mateus', 'nota': 'A'},
    {'nome': 'Maria', 'nota': 'A'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    print(f'Agrupamento: {agrupamento}')
    
    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()
