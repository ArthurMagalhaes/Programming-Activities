#Buy House

price = float(input('\033[30mDeseja comprar uma casa? \nQual o valor do imóvel desejado: R$ '))
salary = float(input('\033[30mQuanto é o seu salário mensal: R$ '))
time = int(input('\033[30mEm quantos anos pretende debitar o empréstimo: '))

mc = price/time/12

if mc <= 0.3*salary:
	print('\033[32mO empréstimo foi aprovado! Você deverá pagar R$ \033[4;32m{:.2f} mensais\033[32m durante os próximos \033[4;32m{} anos\033[32m.'.format(mc,time))
else:
	print('\033[31mSentimos muito em informar que o emprétimo não será aprovado!')
