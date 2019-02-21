#First e last name

name = input('Informe seu nome completo (não esqueça dos espaços):').strip().title()
s = name.split()

print("""\033[30mPrazer em conhecê-lo!
Seu primeiro nome é {}.\033[m
Seu último nome é {}.\033[m""".format("\033[4;32m {}".format(s[0]),"\033[4;31m {}".format(s[name.count(' ')])))
