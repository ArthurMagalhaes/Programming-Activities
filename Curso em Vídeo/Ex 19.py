#Choice a student

import random

stud1 = input('Digite o nome do(a) primeiro(a) estudante:')
stud2 = input('Digite o nome do(a) segundo(a) estudante:')
stud3 = input('Digite o nome do(a) terceiro(a) estudante:')
stud4 = input('Digite o nome do(a) quarto(a) estudante:')
l = [stud1, stud2, stud3, stud4]
c = random.choice(l)
print('Quem apagará o quadro ao final da aula é {}. '.format(c))
