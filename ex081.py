#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.
valores = list()
continuar = ''
contador_cinco = 0

while True:
	numero = int(input('Digite um número: '))
	valores.append(numero)

	while True:
		continuar = str(input('Continuar? ')).strip().upper()

		if 'N' in continuar or 'S' in continuar:
			break

	if 'N' in continuar:
		break

print('=' * (37 + len(str(valores))))
print(f'A quantidade de números digitados é: {len(valores)}')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')

if int(5) in valores:
	print('=' * (37 + len(str(valores))))
	print('O valor "5" está na lista.')
else:
	print('=' * (37 + len(str(valores))))
	print('O valor "5" não está na lista.')

print('=' * (37 + len(str(valores))))
input('pressione ENTER para sair')