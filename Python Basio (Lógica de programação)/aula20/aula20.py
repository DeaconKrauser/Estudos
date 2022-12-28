'''
Operador ternário em Python
'''
logged_user = True

if logged_user:
    msg = 'Usúario logado.'
else

'''
Exibido em operador ternário.
'''
logged_user = True
msg = 'Usuário logado.' if logged_user else 'Usuário precisa fazer logar.'

print(msg)

metodo usando input

idade = input('Qual sua idade? ')

if not idade.isnumeric():
  print('Apenas numeros!')
else:
  idade = int(idade)
  e_de_maior = (idade >= 18)
  msg = 'Pode acessar.' if e_de_maior else 'Não pode acessar.'
print(msg)