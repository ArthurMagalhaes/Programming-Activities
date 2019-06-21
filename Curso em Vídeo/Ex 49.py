#Mathematics Table

n = int(input('Digite um número inteiro:'))

for i in range(1,11):
	if i!=10:
	    print('0{}X{} = {}'.format(i,n,n*i))
	else:
	    print('10X{} = {}'.format(n,n*i))

