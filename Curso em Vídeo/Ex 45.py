#Jakenpô

from random import randint
from time import sleep

num = randint(1,3)

if num==1:
	scomputer = 'PEDRA'
elif num==2:
	scomputer = 'PAPEL'
else:
	scomputer = 'TESOURA'

print('\033[36;47m{:=^60}'.format(' Stone, Paper and Scissor '))
suser = input('\n\033[30mEscolha sua jogada:')
print('\n\033[34mPROCESSANDO...')
sleep(4)

if suser.upper()=='PEDRA' and scomputer=='TESOURA':
	print('\033[32mO computador escolheu TESOURA! Parabéns, você ganhou!')
elif suser.upper()=='PEDRA' and scomputer=='PAPEL':
	print('\033[31mO computador escolheu PAPEL! Você perdeu! Melhor sorte na próxima!')
elif suser.upper()=='PAPEL' and scomputer=='TESOURA':
	print('\033[31mO computador escolheu TESOURA! Você perdeu! Melhor sorte na próxima!')
elif suser.upper()=='PAPEL' and scomputer=='PEDRA':
	print('\033[32mO computador escolheu PEDRA! Parabéns, você ganhou!')
elif suser.upper()=='TESOURA' and scomputer=='PEDRA':
	print('\033[31mO computador escolheu PEDRA! Você perdeu! Melhor sorte na próxima!')
elif suser.upper()=='TESOURA' and scomputer=='PAPEL':
	print('\033[32mO computador escolheu PAPEL! Parabéns, você ganhou!')
elif suser.upper()==scomputer:
	print('\033[33mO computador escolheu {}! Você empatou!'.format(scomputer))
else:
	print('\033[7;33mJOGADA INVÁLIDA\033[m')


