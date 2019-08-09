#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida. -Média abaixo de 5.0: REPROVADO. Média entre 5.0 e 6.9: RECUPERAÇÃO. -Média 7.0 ou superior: APROVADO.
from math import floor
n1 = float(input('Primeira Nota: ')) #nota 1
n2 = float(input('Segunda Nota: ')) #nota 2
m = (n1 + n2) / 2 #média
print('-=' * 20)
if m < 5:
	print('ESTE ALUNO FOI REPROVADO COM A NOTA DE {:.1f}!'.format(m))
elif m >= 5 and m < 7:
	print('ESTE ALUNO FICOU DE RECUPERAÇÃO COM A NOTA DE {:.1f}!'.format(m))
else:
	print('ESTE FOI FOI APROVADO COM A NOTA DE {:.1f}!'.format(m))
print('-=' * 20)
input('pressione ENTER para sair')
