"""
Exibição de valores formatados.

"""
nome = 'Otavio'
idade = 20
altura = 1.70
peso = 85
imc = peso / altura ** 2

print(nome, 'tem', idade, 'de idade e seu imc é', imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc}')

print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))

print('{n} tem {i} anos e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))