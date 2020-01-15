#Faça um programa que jogue par um ímpar com o computador. O jogo só será interrompido quando o jogador PERDER. Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
pontuacao = 0

while True:
	while True:
		par_impar = str(input('PAR OU ÍMPAR? [P/I] ')).upper()

		if 'P' in par_impar or 'I' in par_impar:
			break

	numero = int(input('DIGITE UM NÚMERO: '))
	maquina = randint(0, 11)
	soma = numero + maquina
	print('=' * (32 + len(str(pontuacao))))
	print(f'Eu coloquei {maquina}.\nA SOMA DEU {soma}.')

	if soma % 2 == 0 and 'P' in par_impar:
		pontuacao += 1
		print(f'Você ganhou! A sua pontuação é {pontuacao}.')
		print('=' * (32 + len(str(pontuacao))))

	elif soma % 2 != 0 and 'P' in par_impar:
		print(f'Eu ganhei! A sua pontuação foi {pontuacao}. Fim de jogo.')
		break

	elif soma % 2 == 0 and 'I' in par_impar:
		print(f'Eu ganhei! A sua pontuação foi {pontuacao}. Fim de jogo.')
		break

	elif soma % 2 != 0 and 'I' in par_impar:
		pontuacao += 1
		print(f'Você ganhou! A sua pontuação é {pontuacao}.')
		print('=' * (32 + len(str(pontuacao))))

print('=' * (45 + len(str(pontuacao))))
input('pressione ENTER para sair')