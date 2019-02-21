#Eletronic Radar

velocity = float(input('Qual a velocidade do seu carro neste momento (em Km/h)?'))

if velocity<=80:
	print('\033[33mVocê não será multado!')
else:
	print('\033[1;31mVocê foi multado por exceceder o limite de velocidade! Sua multa é R$ {:.2f}!'.format(7*(velocity-80)))
