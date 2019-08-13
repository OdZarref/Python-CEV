#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A média de idade do grupo. Qual é o nome do homem mais velho. Quantas mulheres têm menos de 20 anos.
media = mulhermenos20 = idadehomemmaisvelho = 0
homemmaisvelho = 'NENHUM'

for c in range(1, 5):
	print(f'DADOS {c}º PESSOA.')
	print('-=' * 8)
	nome = str(input(f'NOME: '))
	idade = int(input(f'IDADE: '))
	sexo = str(input(f'SEXO: [M/F]')).strip().upper()
	media += idade

	if 'F' in sexo:
		if idade < 20:
			mulhermenos20 += 1

	elif 'M' in sexo:
		if idade > idadehomemmaisvelho:
			idadehomemmaisvelho = idade
			homemmaisvelho = nome

	print('-=' * 8)

print(f'A MÉDIA DE IDADE É {media / 4} ANOS.')
print(f'A QUANTIDADE DE MULHERES COM MENOS DE VINTE ANOS É {mulhermenos20}.')
print(f'O NOME DO HOMEM MAIS VELHO É {homemmaisvelho.upper()}.')
print('-=' * 17)
input('pressione ENTER para sair')
