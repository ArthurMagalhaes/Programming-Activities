#Bissext

year = int(input('Digite o valor correspondente a um ano (pode ser negativo caso queira de antes da Era Comum):'))

if year%4==0:
	if year>=0:
		print('\033[32m{} D.C. é um ano bissexto!'.format(year))
	else:
		print('\033[32m{} A.C. é um ano bissexto!'.format(-year))
else:
	if year>=0:
		print('\033[33m{} D.C. {} é um	ano bissexto!'.format(year,'\033[4;33mnão'))
	else:
		print('\033[33m{} A.C. {} é um ano bissexto!'.format(-year,'\033[4;33mnão'))
