"""
condições IF, ELIF e ELSE - aula 4

"""
# if True:
#    print("Verdadeiro.")
#    num_1 = 2
#    num_2 = 4
#    print(num_1 + num_2)

# PARTE 1
if False:
    print('Verdadeiro. ')
    print('teste teste2')
elif True:
    print("Agora é verdadeiro.")
    nome = input("Qual o seu nome?")
    print(f'Seu nome é {nome}.')
elif False:
    print('Mais uma verdadeira.')
    print(22 + 22)
else:
    print("Não é verdadeiro.")
    print("Olá")


# PARTE 2
"""
Operadores Relacionais - Aula 4

"""
'''
TRUE
'''
num_1 = 2 # int
num_2 = '2' # str
print(num_1 == int(num_2))

'''
FALSE
'''
num_1 = 2 # int
num_2 = '2' # str
print(num_1 == num_2)

'''
Outro Metodo
'''
num_1 = 2 # int
num_2 = 2 # int
expressao = (num_1 > num_2)
print(expressao)

#1 metodo
nome = input('Qual seu nome? ')
idade = input('Qual a sua idade? ')
idade = int(idade)
#limite de emprestimo
idade_limite = 18

if idade >= idade_limite:
  print(f'{nome} pode pegar o emprestimo.')
else:
  print(f'{nome} Não pode pegar o emprestimo.')


#2 metodo
nome = input('Qual seu nome? ')
idade = input('Qual a sua idade? ')
idade = int(idade)
#limite de emprestimo
menor_de_idade = 20 #muito jovem
maior_de_idade = 30 #passou dad idade

if idade >= menor_de_idade and idade <= maior_de_idade:
  print(f'{nome} pode pegar o emprestimo.')
else:
  print(f'{nome} Não pode pegar o emprestimo.')

"""
Operadores Lógicos - Aula 4
and, or, not
in e not in
"""
#AND
# (Verdadeiro E False) = Falso
comparacao and comparacao

#OR
# Verdadeiro OU Verdadeiro
comp1_OR_comp2

#NOT
a = 2 
b = 3 

if b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B. ')

a = ''
b = 0

if not a:
    print('Por favor, preecha o valor de A.')

#IN
nome = 'Otavio'

if 'Ota' in nome:
    print("Existe")
else:
    print("Não existe")


#sistema basico de login

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'otavio'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else: 
    print('Usuário ou senha inválidos')

Continuação aula-video = 22