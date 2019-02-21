#Split digits V1

while True:
	number = input('Digite um número natural menor do que 10.000:')
	n = int(number)

	if (n<0 or n>=10000):
		print('O valor está fora do intervalo especificado!')
	elif n<10:
		number = '000'+number
		break
	elif n<100:
		number = '00'+number
		break
	elif n<1000:
		number = '0'+number
		break

print("""Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(number[3],number[2],number[1],number[0]))
