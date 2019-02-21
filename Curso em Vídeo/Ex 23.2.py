#Split digits V2

number = int(input('Digite um número natural menor do que 10.000:'))

print("""Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(number%10,(number%100)//10,(number%1000)//100,number//1000))

