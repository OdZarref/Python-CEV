#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
re1 = float(input('Reta 1: '))
re2 = float(input('Reta 2: '))
re3 = float(input('Reta 3: '))
if re1 < re2 + re3 and re2 < re1 + re3 and re3 < re1 + re2:
	print('É possível formar um triângulo.')
else:
	print('Não é possível formar um triângulo.')
print('-=' * 10)
input('pressione ENTER para sair')
