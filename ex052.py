#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
cont = 0
num = int(input('NÚMERO: '))
print('-=' * 30)
for c in range(1, num + 1):
	if num % c == 0:
		cont += 1
if cont == 2:
	print(f'Este número é primo. Pois foi divisível apenas por 2 números.')
else:
	print(f'Este número foi divisível {cont} vezes. Portanto não é primo.')
print('-=' * 30)
input('pressione ENTER para sair')