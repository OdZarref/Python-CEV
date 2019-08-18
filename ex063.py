#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci. Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8
print('SEQUÊNCIA DE FIBONACCI\nQUANTOS TERMOS QUER VER?')
print('-=' * 10)
numero = int(input('>>> '))
print('-=' * 20)
termo1 = 0
termo2 = 1
termo3 = termo1 + termo2
contador = 2
print(f'{termo1} > {termo2} > ', end='')

while contador != numero :
	termo3 = termo1 + termo2
	termo1 = termo2
	termo2 = termo3

	if contador != numero - 1:
		print(f'{termo3} > ', end='')
	else:
		print(f'{termo3}')
	contador += 1

print('-=' * 20)
input('pressione ENTER para sair')