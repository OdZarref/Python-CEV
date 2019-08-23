#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: A)Qual é o total gasto na compra. B) Quanto produtos custam mais de R$1000. C)Qual é o nome do produto mais barato.
nomemaisbarato = continuar = ''
totalcompra = custammaisdemil = contador = maisbarato = 0

while True:
	nome = str(input('NOME: '))
	preco = float(input('PREÇO: '))

	totalcompra += preco
	contador += 1

	if preco > 1000:
		custammaisdemil += 1

	if contador == 1:
		nomemaisbarato = nome
		maisbarato = preco
	else:
		if preco < maiscaro:
			nomemaisbarato = nome
			maisbarato = preco

	continuar = str(input('QUER CONTINUAR? ')).strip().upper()[0]

	if continuar not in "S":
		break

print(f'CUSTAM MAIS DE 1000: {custammaisdemil}')
print(f'MAIS BARATO: {nomemaisbarato}')
print(f'TOTAL DA COMPRA: {totalcompra}')