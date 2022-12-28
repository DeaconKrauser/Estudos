'''
Dicionarios em py
'''

# 1 metodo
d1 = {'chave1': 'Valor da chave'}
d1['nova_chave'] = 'Valor da nova chave'

print(d1['chave1'])

# 2 metodo
d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
d1['nova_chave'] = 'Valor da nova chave'

print(d1)

# 3 metodo
d1 = { 1: 'Valor', 2: 'Valor', 3: 'Valor'}

print(d1[3])

# 4 metodo
d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla'
}

if 'naoexiste' in d1:
    print(d1['naoexiste'])

print(  d1[(1,2,3,4)]  )

# 5 metodo
d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla'
}

d1['nomedachave'] = 'Agora ela existe'

if d1.get('str') is not None:
    print(d1.get('str'))

print(123)

# 6 metodo
d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla'
}

d1.update({'nova_chave':'novo_valor'})
if d1.get('nova_chave') is not None:
    print(d1.get('nova_chave'))

print(123)

# 7 metodo

d1 = {
    'str' : 'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla'
}

print('str' in d1)
print('str' in d1.keys())
print('valor' in d1.values())

# 8

clientes = {
    'cliente1' : {
        'nome' : 'Otavio',
        'sobrenome':'Willker',
    },
    'cliente2' : {
        'nome' : 'João',
        'sobrenome':'Pereira',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
    

# 9 metodo import
import copy

d1 = { 1: 'a', 2: 'b', 3: 'c'}
v = copy.deepcopy(d1)

v[1] = 'Luiz'
v['d'] [0] = 'João'

print(d1)
print(v)

# 10 metodo

d1 = {
    1: 2,
    2: 3,
    4: 5,
}

d2 = {
    'a' : 'b',
    'c' : 'd',
}
d1.update(d2)
print(d1)