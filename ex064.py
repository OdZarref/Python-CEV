#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
numero = int(input('''[999] SAIR
NÚMERO: '''))
soma = contador = 0
print('-=' * 5)

while numero != 999:
	contador += 1
	soma += numero
	numero = int(input('''[999] SAIR
NÚMERO: '''))
	if numero != 999:
		print('-=' * 5)

print('-=' * 15)
print(f'A SOMA DOS NÚMEROS É {soma}.\nE FORAM DIGITADOS {contador} NÚMEROS.')
print('-=' * 15)
input('pressione ENTER para sair')