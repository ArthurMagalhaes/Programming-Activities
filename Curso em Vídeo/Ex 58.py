#Riddleness Game v2

from random import randint
from time import sleep

comp_number = randint(0,10)
print('\033[35m{:=^20}'.format('Riddleness Game'))
user_number = -1
k = 0
while user_number!=comp_number:
	user_number =  int(input('\n\n\033[30mO computador escolheu um número de 0 a 10. Advinhe qual!\n'))
	k+=1
	print('\033[1;36mPROCESSANDO...\n')
	sleep(2)
	if user_number==comp_number and k==1:
		print('\033[32mVocê acertou na 1ª tentativa! PARABÉNS! Já pensou em ser vidente?')
	elif user_number==comp_number:
		print('\033[33mVocê acertou na {}ª tentativa! PARABÉNS!'.format(k))
	else:
		print('\033[31mVocê errou! Tente novamente!')
