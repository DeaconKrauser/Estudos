'''
Manipulando stings - Aula 6
* Strings indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Pode ser conferido tudo em:
https://docs.python.org/3/library/stdtypes.html (tipos de built-in)
https://docs.python.org/3/library/functions.html (funções built-in)

'''

# positivos  [012345678]
texto =      'Python s2'
print( texto[8] )
# negativos [-987654321]
url = 'www.google.com.br/'
print( url[:-1] )

# fatiamento
nova_string = texto[2:6]
print(nova_string)

# fatiamento
nova_string = texto[-9:-3]
print(nova_string)

# fatiamento
nova_string = texto[0:6:2] # de dois em dois
print(nova_string)


