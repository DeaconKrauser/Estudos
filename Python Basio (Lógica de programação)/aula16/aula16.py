'''
For / Else em python
'''

variavel = ['Otavio', 'Luis', 'Maria']

comeca_com_o = False
for valor in variavel:
    if valor.lower().startswith('O'):
        comeca_com_o = True

if comeca_com_o:
    print('Existe uma palavra que existe com O.')
else:
    print('Não existe uma palavra com O.')


variavel = ['Luiz', 'Joãozinho', 'Maria']

for valor in variavel:
    print(valor)
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra que começa com J')
