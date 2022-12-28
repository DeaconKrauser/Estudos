'''
Funções - def em Python (Parte 1)

'''
# 1
def funcao():
    print('Hello World!')

funcao()

# 2
def saudacao(msg='Olá', nome='Usuario'):
    print(msg, nome)

saudacao()

# 3
def saudacao2(msg='Olá', nome='Usuario'):
    print(msg, nome)

saudacao2(nome='Otavio')

def saudacao(msg='Olá', nome='usuario'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)

saudacao(nome='Zezinho', msg='Hi')
saudacao('Oi', 'Luiz')
saudacao('Hello', 'Maria')