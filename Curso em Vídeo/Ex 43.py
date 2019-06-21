#IMC

weight = float(input('Digite seu  peso (em Kg):'))
height = float(input('Digite sua altura (em m):'))

imc = weight/height**2

print('\033[7;30mSeu I.M.C. é {:.1f}.'.format(imc))
if imc < 18.5:
	print('\033[32;40mVocê está abaixo do peso mínimo necessário para ser considerado saudável({})!'.format(18.5*height**2), end='')
	print('\033[32;40mPrecisa se alimentar melhor!')
elif imc < 25:
	print('\033[33;40mVocê é bastante saudável!')
elif imc < 30:
	print('\033[37;40mVocê está com um pouco de sobrepeso. Talvez esteja na hora de rever seus hábitos alimentares.')
elif imc < 40:
	print('\033[35;40mVocê sofre de obesidade! Você precisa rever seus hábitos urgentemente!')
else:
	print('\033[31;40mVOCÊ SOFRE DE OBESIDADE MÓRBIDA! Procure um médico urgentemente para receber orientação profissional!', end='')
	print('\033[31;40mSua vida está em risco!')
