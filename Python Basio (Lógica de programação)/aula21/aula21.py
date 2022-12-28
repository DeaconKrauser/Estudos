'''
Expressão condicional com o operador OR
'''

nome = input('Qual o seu nome? ')

if nome:
    print(nome)
else:
    print('Voce não digitou nada =(')

metodo utilizando OR.

nome = input('Qual o seu nome? ')

print(nome or 'Voce não digitou nada!=(')


"""
Exercicio.
"""

lista_num = [
    [0,10],
    [1,9],
    [2,8],
    [3,7],
    [4,6],
    [5,5],
    [6,4],
    [7,3],
    [8,2],
]

for indice, valor in lista_num:
    print(indice, valor)


    lista_num = [
    [0,10],
    [1,9],
    [2,8],
    [3,7],
    [4,6],
    [5,5],
    [6,4],
    [7,3],
    [8,2],
]

for indice, valor in enumerate(lista_num):
  print(indice, valor)


Metodo da aula

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)


"""
CPF = 020.881.416-77
---------------------------------
0 * 10 = 0      #  0 * 11
2 * 9 = 18      #  2 * 10
0 * 8 = 0       #  0 * 9
8 * 7 = 56      #  8 * 8
8 * 6 = 48      #  8 * 7
1 * 5 = 5       #  1 * 6
4 * 4 = 16      #  4 * 5
1 * 3 = 3       #  1 * 4
6 * 2 = 12      #  6 * 3

158 

11 - (158 % 11) = 7
11 > 9 = 0
Digito 1 = 0
"""

cpf = input('digite seu cpf: ')
novo_cpf = '02088141677'
cpf_2 = novo_cpf
novo_cpf = cpf

if cpf == novo_cpf:
    print('Valido')
else:
    print('Invalido')
print(novo_cpf)


while True:
    #cpf = '02088141677'
    cpf = input('Digite um cpf: ')
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)
    
    if cpf == novo_cpf:
        print(f'Válido, seu cpf é {novo_cpf}')
        break
    else:
        print('Inválido')
        

