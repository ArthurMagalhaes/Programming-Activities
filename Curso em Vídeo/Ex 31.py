#Tickets

km = float(input('Quantos quilômetros você deverá percorrer em sua viagem?'))

if km <= 200:
	tic = 0.5*km
else:
	tic = 0.45*km
print('Sua passagem custará R$ {:.2f}.'.format(tic))
