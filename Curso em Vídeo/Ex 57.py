#Sex

s = 'T'

while s!='M' and s!='F':
	s = input('\033[30mIndique um sexo (digite \033[4;30mM para masculino\033[30m ou \033[4;30mF para feminino):\033[m\n').strip().upper()
	if s!='M' and s!='F':
		print('\033[31mEntrada não permitida! Faça novamente!\n') 
print('\033[32mValidação executada com sucesso!')
