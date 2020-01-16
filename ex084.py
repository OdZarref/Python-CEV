#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A)Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C)Uma listagem com as pessoas mais leves.
pessoas = list()
dado = list()
nome_mais_pesada = list()
nome_mais_leve = list()
continuar = ''
mais_pesada = mais_leve = contador = contador_quantas_mais_pesadas = contador_quantas_mais_leves = 0
print(f'{"CADASTRO":=^40}')


while True:
	dado.append(str(input('Nome: ')))
	dado.append(float(input('Peso: ')))
	pessoas.append(dado[:])

	if len(pessoas) == 1:
		mais_leve = dado[1]
		mais_pesada = dado[1]
	else:
		if dado[1] < mais_leve:
			mais_leve = dado[1]

		elif dado[1] > mais_pesada:
			mais_pesada = dado[1]
	dado.clear()

	while 'S' not in continuar and 'N' not in continuar:
		continuar = str(input('Continuar? ')).strip().upper()[0]

	if 'N' in continuar:
		break
	continuar = ''


for pessoa in pessoas:
	if pessoa[1] == mais_pesada:
		contador_quantas_mais_pesadas += 1

for pessoa in pessoas:
	if pessoa[1] == mais_leve:
		contador_quantas_mais_leves += 1


print('=' * (39 + len(pessoas)))
print(f'A quantidade de pessoas cadastradas é: {len(pessoas)}')
print('A(s) pessoa mais pesada é: ', end='')
for pessoa in pessoas:
	if contador == contador_quantas_mais_pesadas - 1:
		if pessoa[1] == mais_pesada:
			print(f'{pessoa[0]}.', end='')
	else:
		if pessoa[1] == mais_pesada:
			contador += 1
			print(f'{pessoa[0]}, ', end='')
contador = 0
print('')


print('A(s) pessoa mais leve é: ', end='')
for pessoa in pessoas:
	if contador == contador_quantas_mais_leves - 1:
		if pessoa[1] == mais_leve:
			print(f'{pessoa[0]}.', end='')
	else:
		if pessoa[1] == mais_leve:
			contador += 1
			print(f'{pessoa[0]}, ', end='')
print('')


print('=' * (39 + len(pessoas)))
input('pressione ENTER para sair')