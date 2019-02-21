#Show work

from random import shuffle

s1 = input('Digite o nome do(a) primeiro(a) estudante:')
s2 = input('Digite o nome do(a) segundo(a) estudante:')
s3 = input('Digite o nome do(a) terceiro(a) estudante:')
s4 = input('Digite o nome do(a) quarto(a) estudante:')
l = [s1, s2, s3, s4]
shuffle(l)

print('A ordem de apresentação será ')
print(l)
