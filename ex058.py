#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em uma número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até ele acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
print('TENTE ACERTAR O NÚMERO QUE O COMPUTADOR PENSAR!')
print('-=' * 20)

jogador = int(input('SEU PALPITE? '))
maquina = randint(0, 11)
quantidade_de_tentativas = 0

while jogador != maquina:
	print('-=' * 20)
	quantidade_de_tentativas += 1
	jogador = int(input('ERROU! QUAL SEU NOVO PALPITE? '))

print('-=' * 20)
print(f'VOCÊ ACERTOU! E FORAM NECESSÁRIOS {quantidade_de_tentativas} TENTATIVAS PARA VOCÊ ACERTAR!')
input('pressione ENTER para sair')
