# -*- coding: utf-8 -*-
from random import randint


x = []
while len(x) < 3:
    if len(x) == 0:
       j = randint(1, 9)
    else:
        j = randint(0, 9)
    if j not in x:
        x.append(j)

x = str(x[0]) + str(x[1]) + str(x[2])

print('-'*20)
print('Guess Game')
print('-'*20, end='\n')
y = 0

while y != x:
    y = input('\n\nI have thought in a three digit number with all digits different from each other. '
              'Try do guess which: ')

    # if y < x:
    #     print('I think in a greater number!')
    # elif y > x:
    #     print('I have think in a lower number!')
    c = 0
    m = 0
    for i, j in enumerate(y):
        if j == x[i]:
            m += 1
        elif j in x:
            c += 1

    if c == m == 0:
        print('Nope')
    else:
        if m > 0:
            print('Match')
        if c > 0:
            print('Close')
