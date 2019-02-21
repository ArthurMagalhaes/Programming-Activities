#Santo V2

city = input('Em qual cidade você nasceu?')
city = city.strip().title()

if city.find('Santo')==0:
	print('Você nasceu em uma uma cidade que começa com a palavra Santo.')
else :
	print('Você não nasceu em uma uma cidade que começa com a palavra Santo.')
