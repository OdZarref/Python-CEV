#Crie um programa que tenha uma tupla completamente preenchida com uma contadgem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero_usuario = int(input('Digite um número: [0-20] '))
quantos_iguais = len(str(numeros[numero_usuario]))

if quantos_iguais + 22 > 25: 
	print('=' * (quantos_iguais + 22))
else:
	print('=' * 25)

print(f'Você digitou o número {numeros[numero_usuario].upper()}')

if quantos_iguais + 22 > 25: 
	print('=' * (quantos_iguais + 22))
else:
	print('=' * 25)

input('pressione ENTER para sair')