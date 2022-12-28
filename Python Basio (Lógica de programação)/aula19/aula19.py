''' 
Trocando o valor entre variaveis em Py
'''

x = 10 #Luis
Y =  'Luis' #10

z = x
x = y
y = z

print(f'x={x} e y={y}')

alterando em py 

x = 10 #Luis
y =  'Luis' #10
x, y = y,x

print(f'x={x} e y={y}')


outro metodo.

x = 10 #Luis
y =  'Luis' #10
z = 'Otavio'
x, y, z = z, x, y

print(f'x={x} e y={y} e z={z}')