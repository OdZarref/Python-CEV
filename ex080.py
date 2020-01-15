#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
contador = 1
valores = list()

while contador != 6:
	valor = int(input(f'{"Digite um número: "}'))

	if contador == 1:
		valores.append(valor)

	elif valor > valores[-1]:
		valores.append(valor)

	else:
		for posicao, numero in enumerate(valores):
			if valor <= valores[posicao]:
				valores.insert(posicao, valor)
				break

	contador += 1
print('=' * (36 + len(str(valores))))
print(f'{"Os valores digitados em ordem são: ":-^} {valores}')
print('=' * (36 + len(str(valores))))
input('pressione ENTER para sair')