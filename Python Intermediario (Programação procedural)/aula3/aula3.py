'''
1 - Crie uma função que exibe uma saudação com os parametros saudação e nome.
'''
def saudacao(msg='Olá', nome='Usuario'):
    print(msg, nome)
    
saudacao(nome='Otavio')

'''
2 - Crie uma função que recebe 3 numeros como parametros e exiba a soma entr eles.
'''
def soma(n1, n2, n3):
    if n3 > 0:
        return n1 + n2 + n3
resultado = soma(10,10,10)
if resultado:
    print(f'A some entre os valores é {resultado}')
else:
    print('Conta invalida!')

'''
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%).
Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo.
'''

def percentual(n1, n2, n3):
    if n2 > 0:
        return (n1 + n2) % n3
resultado = percentual(10)
if resultado:
    print(f'O percentual é {resultado}')
else:
    print('Conta invalida!')

'''
4 - Fizz Buzz - Se o parametro da função for divisivel por 2, retorne fizz,
se o parametro da função for divisivel por 5, retorne buzz. Se o parametro da 
função for divisivel por 5 e por 3, retorne FizzBuzz, caso contrario, retorne o número enviado.
'''

