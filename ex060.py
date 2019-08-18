#Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5!=5x4x3x2x1 = 120
numero = int(input('NÚMERO: '))
contador = numero
resultado = numero
print('-=' * 13)
print(numero, end='')

while contador != 1:
	contador -= 1
	resultado = resultado * contador
	print(f'x{contador}', end='')

print(f'={resultado}')
print('-=' * 13)
input('pressione ENTER para sair')