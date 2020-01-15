#Faça um programa que leia cinco valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
print(f'{"DIGITE 5 NÚMEROS":=^55}')
valores = [int(input('1°: ')), int(input('2°: ')), int(input('3°: ')), int(input('4°: ')), int(input('5°: '))]
contador = maior = menor = 0

for valor in valores:
	contador += 1

	if contador == 1:
		maior = menor = valor
	else:
		if valor > maior:
			maior = valor

		elif valor < menor:
			menor = valor

contador = 0
print('=' * (55 + len(str(maior))))
print(f'Os valores digitados foram {valores}.')
print(f'Sendo o maior valor foi {maior} na(s) posição(ções) ', end='')

for posicao, valor in enumerate(valores):
	if valor == maior:
		print(f'{posicao}...', end='')

print(f'\nSendo o menor valor {menor} na(s) posição(ções) ', end='')

for posicao, valor in enumerate(valores):
	if valor == menor:
		print(f'{posicao}...', end='')

print('')
print('=' * (55 + len(str(maior))))
input('pressione ENTER para sair')