#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
year = int(input('Digite um ano: '))
if year % 100 == 0:
	if year % 400 == 0:
		print('Este ano é bissexto.')
	else:
		print('Este não é um ano bissexto.')
else:
	if year % 4 == 0:
		print('Este ano é bissexto.')
	else:
		print('Este ano não é bissexto.')
print('-=' * 10)
input('pressione ENTER para sair')