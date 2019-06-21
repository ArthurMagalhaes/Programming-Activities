#Pay Manager´s

cost = float(input('Qual o valor da compra? '))

while True:

	print('Escolha a opção de pagamento:\n')

	print('[1] Pagamento à vista em espécie/cheque')
	print('[2] Pagamento à vista no cartão')
	print('[3] Pagamento 2X no cartão')
	print('[4] Pagamento 3X no cartão ou mais')

	op = int(input(''))

	if op==1:
		pag = 0.9*cost
		print('O valor final da compra será R$ {:.2f}'.format(pag))
		break
	elif op==2:
		pag = 0.95*cost
		print('O valor final da compra será R$ {:.2f}'.format(pag))
		break
	elif op==3:
		pag = cost
		print('O valor final da compra será R$ {:.2f}'.format(pag))
		break
	elif op==4:
		pag = 1.2*cost
		print('O valor final da compra será R$ {:.2f}'.format(pag))
		break
	else:
		print('Opção inexistente!\n')

