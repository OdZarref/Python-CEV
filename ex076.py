#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
contador = 0
tupla = ('Arroz', 10.50, 'Feijão', 12.50, 'Caixa de Ovos', 10, 'Manteiga', 5, 'Chinelo', 13, 'Óleo', 5, 'Macarrão', 8, 'Bananas', 5, 'Toddy', 10)
print(f'{"LISTA DE PREÇOS":=^31}')

for itens in tupla:
	contador += 1

	if contador % 2 == 1:
		print(f'{itens:.<20}', end='')
	else:
		print(f' = R${itens: >6.2f}')

print('=' * 31)
input('pressione ENTER para sair')