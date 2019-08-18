#Crie um programa que leia dois valores e mostre um menu na tela: [1] somar: [2] multiplicar: [3] maior: [4] novos números: [5] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.
valor1 = int(input('PRIMEIRO NÚMERO: '))
valor2 = int(input('SEGUNDO NÚMERO: '))
opcao = 0

while opcao != 5:
	opcao = int(input('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR
>>>>>'''))
	print('-=' * 20)

	if opcao == 1:
		print(valor1 + valor2)
		print('-=' * 20)
	elif opcao == 2:
		print(valor1 * valor2)
		print('-=' * 20)
	elif opcao == 3:
		if valor1 > valor2:
			print(valor1)
			print('-=' * 20)
		elif valor2 > valor1:
			print(valor2)
			print('-=' * 20)
		elif valor1 == valor2:
			print('AMBOS SÃO IGUAIS.')
			print('-=' * 20)
	elif opcao == 4:
		valor1 = int(input('DIGITE O PRIMEIRO NÚMERO: '))
		valor2 = int(input('DIGITE O SEGUNDO NÚMERO: '))
		print('-=' * 20)
	elif opcao == 5:
		print('FIM DO PROGRAMA')
	else:
		print('OPÇÃO INVÁLIDA!')

print('-=' * 20)
input('pressione ENTER para sair')