#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = menor = 0

for c in range (1, 6):
	peso = float(input(f'PESO DA {c}º PESSOA: '))

	if c == 1:
		maior = peso
		menor = peso

	else:
		if peso > maior:
			maior = peso

		if peso < menor:
			menor = peso

print('-=' * 16)
print(f'''O MAIOR PESO LIDO FOI {maior} KG.
O MENOR PESO LIDO FOI {menor} KG.''')
print('-=' * 16)
input('pressione ENTER para sair')
