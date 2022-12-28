from dados import produtos, pessoas, lista

# map = recebe uma função como primeiro argumento.

#nova_lista = iter(lambda x: x *2, lista)
#nova_lista = [x * 2 for x in lista]
#print(lista)
#print(list(nova_lista))

#def aumenta_preco(p):
#    p['preco'] = round(p['preco'] * 1.05, 2)
#    return p

#DICIONARIO
#novos_produtos = map(aumenta_preco, produtos)

#for produto in novos_produtos:
    #print(produto)


#for preco in precos:
#   print(preco)

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p

nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)