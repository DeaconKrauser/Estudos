variavel = 'valor'

def func():
    print(variavel)

def func2():
    global variavel
    variavel = 'Outro valor'
    print(variavel)

    
def func2(arg=Nome):
    arg = arg.replace('V', 'c')
    return arg

func()
outra_variavel = func2(arg=variavel)    

func2()

variavel = 'Valor'

def func():
    outra_variavel = 'Valor'
    return outra_variavel

def func2(arg):
    print(arg)

var = func()
func2(var)

'''
1 - Crie uma função1 que recebe uma função2 como parametro e retorne da função2 executada.
'''

def hello_world():
    return 'Olá mundo!'

def result(funcao):
    return funcao()

executando = result(hello_world)
print(executado)

'''
2 - Crie uma função1 que recebe uma função2 como parametro e retorne o valor da função2 executada. 
Faça a função1 executar duas funções que recebam um número diferente de argumentos.
'''
  
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'Otavio')
executando2 = mestre(saudacao, 'Otavio', saudacao='Bom dia!') 
print(executando)
print(executando2)

