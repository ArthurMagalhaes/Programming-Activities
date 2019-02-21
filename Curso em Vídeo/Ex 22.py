#String Parser

name = input('Informe seu nome completo:')

print(name.upper())
print(name.lower())
print('Seu nome contém {} letras.'.format(len(name)-name.count(' ')))
print('Seu primeiro nome possui {} letras'.format(len(name.split()[0])))
