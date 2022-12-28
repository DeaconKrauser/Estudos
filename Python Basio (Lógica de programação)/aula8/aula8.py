"""
Proxima aula 16 

* Criar variaveis para nome (str), idade(int),
* altura (float) e peso (float) de uma pessoa
* Criar variavel com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)

"""

#Nome - Idade - Altura
nome = 'Otavio'
idade = 20
altura = 1.70

#Ano atual 
ano_atual = 2019

#Ano de nascimento
date_nasc = ano_atual - idade

#IMC

imc = peso / altura ** 2


print (f'{N} tem {I} anos e tem {A:.2f}'.format(N=nome, I=idade, A=altura,))
print (f'{N} nasceu no ano de {D}'.format(N=nome, D=date_nasc))
print (f'O seu IMC é {IM}'.format(IM=imc))



name = 'Otavio'
nacionalidade = 'Brasileiro'
estado_civil = 'Solteiro'
idade = 20
de_maior = idade > 18
de_menor = idade < 18

#
altura = 1.70
peso = 85.5
imc = peso / altura ** 2

# 
data_nascimento = 1999
data_atual = 2019
resultado = data_atual - idade

print('Olá {n}, validei aqui e estou vendo que voce tem {i} anos e seu imc é {im:.2f}'.format(n=name, i=idade, im=imc))
print('Validei tambem que voce nasceu no ano de {date} e seu estado civil é {civil}'.format(date=data_nascimento, civil=estado_civil))
print('E seus dados afirmam que voce é {maior}'.format(maior=de_maior, menor=de_menor))



idade = 17
maior_menor = 18

if idade > maior_menor:
  print('voce é maior de idade')
elif idade == maior_menor:
  print('voce é maior de idade')
else:
  print('voce é menor de idade')