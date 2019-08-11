#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
termo = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))
for c in range(1, 11):
	print(f'{c:2}º = {termo}')
	termo += razao
print('-=' * 13)
input('pressione ENTER para sair')