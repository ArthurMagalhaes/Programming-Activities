#Dissecting a variable

var = input('Digite algo')

print(type(var))

print('Numérico', var.isnumeric())
print('Alfabético', var.isalpha())
print('Alfanumérico', var.isalnum())
print('Somente espaços', var.isspace())
print('Maiúsculo', var.isupper())
print('Minúsculo', var.islower())
print('Capitalizado', var.istitle())
