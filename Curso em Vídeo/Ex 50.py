#Add Pairs

s = 0

for i in range(0,6):
	n = int(input('Digite um número inteiro:'))
	if n%2==0:
		s+=n

print('\033[7;31mA soma dos pares digitados é {}'.format(s))
