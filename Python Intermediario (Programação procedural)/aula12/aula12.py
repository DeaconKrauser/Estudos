"""
Geradores, Iteradores e iteraveis em py

"""
#UM ITERADOR VAI TE DAR UM VALOR UNICO SEMPRE QUE PRECISAR
lista = [0,1,2,3,4,5]
lista = iter(lista)

#RETORNARA O VALOR DA LISTA
print(next(lista))
print(next(lista))
print(next(lista))

print(hasattr(lista, '__next__'))


import sys
lista = list(range(10))

#sys.getsizeof = quantos mb ram está sendo consumindo ao executar o cod.
print(sys.getsizeof(lista))

#METODO DE GERADORES

import sys 
import time

def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.2)
    return r

g = gera()

for v in g:
    print(v)


#OUTRO METEDO DE GERADOR

def gera():
    for n in range(100):
        yield n
        time.sleep(0.2)

g = gera()

for v in g:
    print(v)

----------------------------------
import sys 
import time

def gera():
    for n in range(100):
        yield n
        time.sleep(0.2)

print(sys.getsizeof(gera))
g = gera()

for v in g:
    print(v)

--------------------------------

import sys
import time

lista = [x for x in range(1000)] #LISTA / Vão reter todos os valores e salvar na memoria.
print(type(lista)) 
lista = (x for x in range(1000)) #GERADOR / vão reter todos os valores, porem não vão salvar na memoria.
print(type(lista))


"""
Exercicios!
SOMANDO O TOTAL COM LIST COMPREHENSION
"""
valor_total = []

valor_total.append(('Compra1', 150.90))
valor_total.append(('Compra2', 299.71))
valor_total.append(('Compra3', 195.49))


soma_total = sum([b for b in valor_total])
print(soma_total)

/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

nome = input('Digite seu nome: ')

carrinho = []
carrinho.append(('Comrpa1', 35.50))
carrinho.append(('Comrpa1', 19.70))
carrinho.append(('Comrpa1', 45.80))

valor_total = sum([float(a,b) for a, b in carrinho])
print(f'Olá {nome}, verifiquei aqui e a soma total do seu carrinho é R${valor_total} reais.')