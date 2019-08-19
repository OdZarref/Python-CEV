#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
soma = contador = 0

print('DIGITE VÁRIOS NÚMEROS. [999] para parar')

while True:
	print('-=' * 20)
	numero = int(input('>>> '))

	if numero == 999:
		break

	soma += numero
	contador += 1

print('-=' * 20)
print(f'A SOMA DOS NÚMEROS É {soma}.')
print(f'FORAM DIGITADOS {contador} NÚMEROS.')
print('-=' * 20)
input('pressione ENTER para sair')