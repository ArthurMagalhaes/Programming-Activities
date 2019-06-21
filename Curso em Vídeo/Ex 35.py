#Triangule Condition

side1 = float(input('Digite o comprimento do 1º segmento de reta:'))
side2 = float(input('Digite o comprimento do 2º segmento de reta:'))
side3 = float(input('Digite o comprimento do 3º segmento de reta:'))

if (side1+side2>side3) and (side1+side3>side2) and (side2+side3>side1):
	print('\033[1;35mOs segmentos dados cumprem a condição de existência, isto é, podem ser arranjados de forma a constituiurem um triângulo.')
else:
	print('\033[1;33mOs segmentos dados não cumprem a condição de existência, isto é, não podem ser arranjados de forma a constituirem um triângulo.')
