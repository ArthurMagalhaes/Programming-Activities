#Salary

employee = input('Digite o nome do(a) funcionário(a).').strip()
salary = float(input('Digite o salário atual de {}. R$ '.format(employee)))

print('Após o aumento, {} terá um salário de R$ {:.2f}.'.format(employee,(1.15*salary)))
