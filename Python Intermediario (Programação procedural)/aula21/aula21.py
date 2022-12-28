"""
Uso de try e except como condicional
"""




def saudacao2(msg='Olá', nome='Usuario', msg2='Bem-vindo ao multiplicador' ):
    return msg, nome, msg2

while True:
    nome = saudacao2(input('Digite seu nome: '))

    if nome is None:
        print('Erro')
    else:
        print(f'{nome}')

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass
        
    
while True:
    numero = converte_numero(input('Digite um numero: '))

    if numero is None:
        print('Erro: Isso não é um numero')
    else:
        print(numero * 2)