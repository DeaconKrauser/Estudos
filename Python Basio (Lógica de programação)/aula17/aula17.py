'''
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str 
* Enumerate - Enumerar elementos da lista # list
'''

string = "O Brasil é o pais do futbol, o Brasil é penta"
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_1:
  print( f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase' )


string = "O Brasil é o pais do futbol, o Brasil é penta"
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_1:
  qtd_vezes = lista_1.count(valor)

  if qtd_vezes > contagem:
    contagem = qtd_vezes
    palavra = valor

print(f' A palavra que apareceu mais vezes é {palavra} ({contagem}x)')


metodo join..

string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ','.join(lista)

print(string)
print(lista)
print(string2)

string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
  print(indice, valor, lista[indice])

  lista = [
  [0,'Luis'],
  [1,'João'],
  [2,'Otavio'],
]

for indice, nome in lista:
  print(indice, nome) // desempacotamento dos valores na lista.