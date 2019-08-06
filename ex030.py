#Crie um programa que leia um número inteiro e mostre na tela e mostre se ele é par ou ímpar.
num = int(input('Digite um número: '))
if num % 2 == 0:
	print('Este número é PAR.')
else:
	print('Este número é ÍMPAR.')
print('-=' * 10)
input('pressione ENTER para sair')