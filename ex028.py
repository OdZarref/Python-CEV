#ex028: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
player = int(input('Digite um número de 0 a 5: '))
choice = randint(0, 5)
if player == choice:
	print(f'Você ganhou! Eu escolhi {choice}.')
else:
	print(f'Você perdeu! Eu escolhi {choice}.')
print('-=' * 10)
input('pressione ENTER para sair')