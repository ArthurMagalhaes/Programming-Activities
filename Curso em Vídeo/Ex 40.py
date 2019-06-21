#Stack

name = input('\033[1;32mDigite o nome do(a) aluno(a)') 
n1 = float(input('\033[1;32mDigite a primeira nota do(a) aluno(a)'))
n2 = float(input('\033[1;32mDigite a segunda nota do(a) aluno(a): '))
stack = (n1+n2)/2

if stack < 5:
	print('\n\033[31;40mA média do(a) aluno(a) {} é {:.1f}. O(A) Aluno(a) está \033[4;31;40mreprovado(a)\033[4;31;40m!\033[m'.format(name, stack))
elif stack >= 5 and stack < 7:
	print('\n\033[33;40mA média do(a) aluno(a) {} é {:.1f}. O(A) Aluno(a) está em \033[4;33;40mrecuperação\033[4;33;40!\033[m'.format(name, stack))
else:
	print('\n\033[32;40mA média do(a) aluno(a) {} é {:.1f}. O(A) Aluno(a) está \033[4;32;40maprovado(a)\033[4;32;40m!\033[m'.format(name, stack))
