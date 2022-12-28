'''
Formatando valores com modificadores - Aula 5

:s - Texto (Strigns)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(Número)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita 
^ - Centro

'''

#metodo 1
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print( '{:.2f}'.format(divisao))

#metodo 2
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print( f'{divisao:.2f}'.)

#metodo com Strings
nome = 'Otavio'
print(f'{nome:s})

#metodo com quantidade de casas decimais.
num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0<10}')

num_2 = 1150
print(f'{num_2:0>10.2f}')

nome = 'Otavio Willker'
print( (50-len(nome)) / 2 )
print(f'{nome:#^50}')

nome = 'Otavio Willker'
nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)

'''
nome = input('Digite seu email: ')
nome_formatado_via_email = '{:@>50}'.format(nome)
print(nome_formatado_via_email)
'''

"""
#metodo login: 

email = input('Digite seu email: ')
email_2 = 'gmail.com'
caracter = '{:@>10}'.format(email_2)
print( email + caracter)
"""

email = 'otaviowillkergmail.com.br'
nome_formatado = '{n:0<20}'.format(n=nome)
print(nome_formatado)

#outros metodos
nome = 'Otavio Willker'
nome = nome.ljust(20, '#')
print(nome)
nome = 'otaviowillker'
nome = nome.ljust(14, '@')
print(nome)

nome = 'Otavio Willker'
print(nome.lower()) #tudo minusculo
print(nome.upper()) #tudo maiusculo
print(nome.title()) #Primeira letra maiuscula
