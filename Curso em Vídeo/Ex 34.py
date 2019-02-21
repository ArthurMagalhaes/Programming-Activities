#Salary

name = input('Digite o nome de um funcionário:')
olds = float(input('Digite o salário atual do(a) {}: R$'.format(name)))

if olds>12500:
	news = olds*1.1
else:
	news = olds*1.15

print('O salário de {} será atualizado e ele(a) passará a receber R${:.2f}.'.format(name,news))
