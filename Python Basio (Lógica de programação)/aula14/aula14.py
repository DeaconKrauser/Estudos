'''
while / else - aula 8
contadores
acumuladores
'''

contador = 0 

while contador < 100:
print(contador)
contador +=1

contador = 1 
acumulador = 1

while contador < 100:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador +=1
else: 
    print('Cheguei no else.')
print('Isso será executado')

"""
Iterando strigns com while em python

"""

while True:
    minha_string = input('Digite uma frase: ')
    tamanho_string = len(minha_string)

    c = 0
    contagem_atual = 0
    letra = ''
    while c < tamanho_string:
        qtd_vezes_letra = minha_string.count(minha_string[c])
        
        if contagem_atual < qtd_vezes_letra and minha_string[c].strip():
            letra = minha_string[c]
            contagem_atual = qtd_vezes_letra
            
        c += 1 
    print(letra, contagem_atual)


'''
For in em Python
Interando strings com For
Função range(start=0, stop, step=1)

'''

texto = 'Python'

for letra in texto:
    print(letra)

#enumerando cada volta no laço for
texto = 'Python'

for n, letra in enumerate(texto):
    print(n, letra)

Função Range
for n in range(20 #começaem20, 10#finalizaem10, -1#pulade1em1):
    print(n)

#Outro exemplo:
for n in range(0, 100, 8):
    print(n)
    
print('################')

for n in range(100):
    if n % 8 == 0:
        print(n)


#alterando apenas certas letras da variavel.

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)

    