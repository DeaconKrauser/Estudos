"""
Zip - Unindo iteráveis
Zip_longest - Itertools

"""

### Código
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
### Código
estados = ['SP', 'MG', 'BA']
cidade_estado = zip(cidades, estados)

print(next(cidade_estado))

--------------------------------
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']
cidade_estado = zip(cidades, estados)

for valor in cidade_estados:
    print(valor)

--------------------------------
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']
cidade_estado = zip(estados, cidades)

print(dict(cidade_estado))

--------------------------------
from itertools import zip_longest, count

indice = count()

cidades = [
    'São Paulo', 
    'Belo Horizonte', 
    'Salvador', 
    'Monte Belo'
    ]

estados = [
    'SP', 
    'MG', 
    'BA'
    ]

cidade_estado = zip_longest(
    indice,
    estados, 
    cidades, 
    fillvalue='Estado'
    )

for indice, estado, cidade in cidade_estado:
    print(indice, estado, cidade)

----------------------------------
#ZIP_LONGEST com COUNT entra em conflito.
from itertools import zip_longest, count

indice = count()

cidades = [
    'São Paulo', 
    'Belo Horizonte', 
    'Salvador', 
    'Monte Belo'
    ]

estados = [
    'SP', 
    'MG', 
    'BA'
    ]

cidade_estado = zip(
    indice,
    estados, 
    cidades,
    )

for indice, estados, cidades in cidade_estado:
    print(indice, estado, cidade)


----------------------------

from types import GeneratorType

variavel = zip('Alo') #string iteravel
print(list(variavel)) #retorna um iterador
print(next(variavel)) #retorna um valor de cada vez

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

from types import GeneratorType

variavel = ((x,y) for x, y in zip('Alo'))

print(isinstance(variavel, GeneratorType))
print(list(variavel))