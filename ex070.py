#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: A) Qual é o total gasto na compra. B) Quantos Produtos custam mais de R$1000. C) Qual é o nome do produto mais barato.
contador = quantidade_mais_mil = preco_total = preco_mais_barato = 0
nome_produto_mais_barato = ''
print(f'{"MERCADO DO ZEZÃO":=^52}')

while True:
	continuar = ''
	contador += 1
	nome = str(input('Produto: '))
	preco = float(input('Preço: '))
	preco_total += preco

	if preco > 1000:
		quantidade_mais_mil += 1

	if contador == 1:
		nome_produto_mais_barato = nome
		preco_mais_barato = preco
	else:
		if preco < preco_mais_barato:
			preco_mais_barato = preco
			nome_produto_mais_barato = nome

	while 'S' not in continuar and 'N' not in continuar:
		continuar = str(input('Continuar? ')).strip().upper()[0]

	print('=' * (51 + len(str(quantidade_mais_mil))))

	if continuar == 'N':
		break


print(f'{"FIM DO PROGRAMA":=^52}')
print(f'O total da compra é: R${preco_total:.2f}')
print(f'A quantidade de produtos que custam mais de mil é: {quantidade_mais_mil}')
print(f'O nome do produto mais barato é: {nome_produto_mais_barato}')
print('=' * (51 + len(str(quantidade_mais_mil))))
input('pressione ENTER para sair')