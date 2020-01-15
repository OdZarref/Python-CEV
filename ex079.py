#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.  Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = list()

while True:
	continuar = ''

	while True:
		valor = int(input('Digite um número: '))

		if valor not in valores:
			valores.append(valor)
			print('Adicionado com sucesso.')
			print('=' * 23)
			break
		else:
			print('Número duplicado. Tente novamente.')
			print('=' * 34)

	while 'S' not in continuar and 'N' not in continuar:
		continuar = str(input('Continuar? ')).upper()

	if 'N' in continuar:
		break

print('=' * (45 + len(str(valores))))
print(f'Os valores digitados em ordem crescente são: {sorted(valores)}')
print('=' * (45 + len(str(valores))))
input('pressione ENTER tecla para sair')