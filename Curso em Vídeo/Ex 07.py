#Stack

name = input('\033[1;32mDigite o nome do(a) aluno(a)') 
n1 = float(input('\033[1;32mDigite a primeira nota do(a) aluno(a)'))
n2 = float(input('\033[1;32mDigite a segunda nota do(a) aluno(a): '))

print('\n\033[7mA média do(a) aluno(a) {} é {:.1f}.\033[m'.format(name, (n1+n2)/2))
