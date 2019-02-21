#Greater and less

n1 = int(input('Digite o primeiro inteiro:'))
n2 = int(input('Digite o segundo inteiro:'))
n3 = int(input('Digite o terceiro inteiro:'))

l = n1
g = n1
#Comparando n1 e n2
if n1<n2:
	g = n2
else:
	l = n2
#Comparando g e l com n3
if g<n3:
	g = n3
if l>n3:
	l = n3

print('O maior e o menor dos 3 são, respectivamente, {} e {}.'.format(g,l))
