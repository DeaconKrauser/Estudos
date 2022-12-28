'''
Faça um programa que peça o usuario para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número 
inteiro, informa que não é um número inteiro.

'''
numero_inteiro = input('Digite um numero inteiro: ')

if not numero_inteiro.isdigit():
  print(f'Isso não é um número inteiro')
else:
  numero_inteiro = int(numero_inteiro)

if not numero_inteiro % 2 == 0:
  print(f'{numero_inteiro} é impar')
else: 
  print(f'{numero_inteiro} é par')



'''
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite. 18-23
'''

nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 4:
  print('Seu nome é curto.')
elif tamanho <= 6:
  print('Seu nome é normal.')
else: 
  print('Seu nome é muito grande.')


'''
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "seu nome é muito grande".

'''

horario = input('Digite um horario (0-23): ')

if horario.isdigit():
  horario = int(horario)
  
  if horario < 0 or horario > 23:
    print("Horário deve estar entre 0 e 23")
  else:
    if horario <= 11:
      print('Bom dia!')
    elif horario <=17:
      print('Boa tarde!')
    else:
      print('Boa noite!')
else:
    print("Por favor, digite um horário entre 0 e 23.")

