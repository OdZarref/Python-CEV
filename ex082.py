#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista_completa = list()
lista_pares = list()
lista_impares = list()
continuar = ''

while True:
	numero = int(input('Digite um número: '))
	lista_completa.append(numero)

	if numero % 2 == 0:
		lista_pares.append(numero)
	else:
		lista_impares.append(numero)

	while True:
		continuar = str(input('Continuar? ')).strip().upper()

		if 'S' in continuar or 'N' in continuar:
			break

	if 'N' in continuar:
		break

print('=' * (16 + len(str(lista_completa))))
print(f'Lista completa: {lista_completa}')
print(f'Lista de pares: {lista_pares}')
print(f'Lista de impares: {lista_impares}')
print('=' * (16 + len(str(lista_completa))))
input('pressione ENTER para continuar')