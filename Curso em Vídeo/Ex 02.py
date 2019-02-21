#Birthday

day = input('Dia = ')
month = input('Mês = ')
year = input('Ano = ')

print('Você nasceu em ', day, '/', month, '/', year, '. Correto?')
print('\033[35mVocê nasceu em \033[4;32m{}/{}/{}.\033[35m Correto?'.format(day,month,year))
