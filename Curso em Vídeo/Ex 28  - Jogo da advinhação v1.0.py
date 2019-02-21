#Riddleness Game

from random import randint
from time import sleep

comp_number = randint(0,5)
user_number = int(input('\033[30mO computador determinou um número de 0 a 5. Advinhe qual!'))
print('\033[1;33mPROCESSANDO...')
sleep(4)

if user_number == comp_number:
	print('\033[32mVocê acretou! PARABÉNS! Já pensou em ser vidente?')
else:
	print('\033[31mVocê errou! Eu pensei no número {}. Melhor sorte na próxima!'.format(comp_number))
