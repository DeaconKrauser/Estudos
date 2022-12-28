from dados import produtos, pessoas, lista

#FILTER = retorna true ou false

#nova_lista = filter(lambda x: x > 5)
#nova_lista = [x for x in lista if x > 5]

# FUNCAO RETORNANDO O VALOR MAIOR QUE 50R$
def filtra(produto):
    if produto['preco'] > 50:
        return True
    

nova_lista = filter(filtra, produtos)
for produto in nova_lista:
    print(produto)


#/*/*/*/*/*/*/*/*/*/*/*/*/*


def filtra(produto):
    if produto['preco'] > 50:
        produto['e_caro'] = True
        return True
    

nova_lista = filter(filtra, produtos)

for produto in nova_lista:
    print(produto)


#/*/*/*/*/*/*/*/*/*/*/*/*/*/*

def filtra(produto):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False

nova_lista = filter(filtra, pessoas)

for produto in nova_lista:
    print(produto)