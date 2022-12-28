'''
while em python - aula 7
utilizado para realizar ações enquanto uma condição for verdadeira.

requisitos: Entender condições e operadores.
'''

x = 0
while x < 100:
    print(x)
    x = x + 1
print('Acabou!')

# continue(pula o proximo loop)
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue

    print(x)
    x = x + 1

print('Acabou!')

# break(para apos o loop)
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break

    print(x)
    x = x + 1

print('Acabou!')


x = 0 # coluna
while x < 10:
    y = 0 # linha

    while y < 5:
        print(f'({x},{y}))
        y += 1
    x += 1 # x = x + 1
print('Acabou!')

# Calculadora
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break

    if not  num_1.isnumeric() or not num_2.isnumeric():
        print('Voce precisa digitar um numero!')
        continue
    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / * 
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido')
