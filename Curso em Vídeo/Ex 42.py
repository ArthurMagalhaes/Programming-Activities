#Triangule 

side1 = float(input('Digite o comprimento do 1º segmento de reta:'))
side2 = float(input('Digite o comprimento do 2º segmento de reta:'))
side3 = float(input('Digite o comprimento do 3º segmento de reta:'))

if (side1+side2>side3) and (side1+side3>side2) and (side2+side3>side1):
	print('\033[1;35mOs segmentos dados cumprem a condição de existência, isto é, podem ser arranjados de forma a constituiurem um triângulo.')
	if side1==side2 and side1==side3:
		print('\033[1;32mO triângulo em questão é equilátero.')
	elif side1==side2 or side1==side3 or side2==side3:
		print('\033[1;34mO triângulo em questão é isóceles.')
	else:
		print('\033[1;30mO triângulo em questão é escaleno.')
else:
	print('\033[1;33mOs segmentos dados não cumprem a condição de existência, isto é, não podem ser arranjados de forma a constituirem um triângulo.')

