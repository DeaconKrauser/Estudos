# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

s1 = set()
s1.add(1) #adicionando
s1.discard(1) #removendo
s1.update({2,3}) # atualizando

print(s1)

#Removendo a duplicidade da lista.

l1 = [1,2,1,1,3,4,5,6,6,6,6,6,7,8,9, 'Otavio','Otavio']
l1 = set(l1)

print(l1)

#Metodo unir
union | une

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2

print(s3)

#2 modulo 
s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 & s2

print(s3)

#3 modulo

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 - s2

print(s3)

#4 modulo
s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 ^ s2

print(s3)

l1 = ['Luiz', 'Otavio', 'Maria', 'João']
l2 = ['João', 'Maria', 'Maria', 'Otavio', 'Otavio', 'Otavio', 'Luiz', 'Luiz']

if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')