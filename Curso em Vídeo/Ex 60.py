#Factorial

n = int(input('Digite um número natural:'))
f = 1
c = n
if n<0:
	print('Não existe fatorial de números negativos!')
elif n<=1:
	print('O fatorial de {} é 1!'.format(n))
else:
	while c>1:
		f*=c
		c-=1
	print('O fatorial de {} é {}'.format(n,f))
