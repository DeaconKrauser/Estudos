'''
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range

'''

#metodo 1

#         0    1    2    3    5
lista = ['A', 'B', 'C', 'D', 'E']
#  -      5    4    3    2    1

string = 'ABCDE'

print(string[1])



#metodo 2

#         0    1    2    3    5
lista = ['A', 'Bacana', 'D', 'E']
#  -      5    4    3    2    1

string = 'ABCDE'

print(lista[1])

#metodo 3 alterando valores nas indices.

#         0    1    2    3    4    5
lista = ['A', 'B', "C", 'D', 'E', 10.5]
lista[5] = 11

print(lista[5])

#         0    1    2    3    4    5
lista = ['T', 'e', 'S', 'T', 'e', '1']
lista[0:8] = 'Testando'
#   [Começo: Fim: Salto]
print(lista[0:8])


# Insert 

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2

print(l3)
------------

l1 = [1,2,3]
l2 = [4,5,6]
l2.insert(0, 'Morango')

print(l1)

# extend
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)

print(l1)

# append inseri sempre no final da lista
l1 = [1,2,3]
l2 = [4,5,6]
l2.append('b')

print( l2[3] )

# del

l2 = [4,5,6]
print(l2)
l2.insert(0, 'morango')
print(l2)
l2.pop()
print(l2)

#     0 1 2 3 4 5 6 7 8
l2 = [1,2,3,4,5,6,7,8,9]
print(l2)
l2.insert(0, 'Morango')
print(l2)
del(l2[0])
print(l2)

# max / min 
#     0 1 2 3 4 5 6 7 8
l2 = [1,2,3,4,5,6,7,8,9]

print( max(l2) )
print( min(l2) )

#listando valores sem precisar digitar de 1 a 10
l2 = list(range(1,10))
print(l2)
print( max(l2) )
print( min(l2) )

l2 = ['String', True, 10, -20.5]

for elem in l2:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')


#outro metodo

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Voce perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print('Letra corresponde aos dados!')
    else:
        print('Letra não encontrada!')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Palavra encontrada!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
    
    print(f'Voce ainte tem {chances} chances.')
    print()

