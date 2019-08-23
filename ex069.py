#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) Quantas pessoas tem mais de 18 anos. B) Quantos homens foram cadastrados. C) Quantas mulheres tem menos de 20 anos.
print('-=' * 20)
print('DIGITE OS DADOS PARA CADASTRO')
print('-=' * 20)
mais18 = mulhermenos20 = homens = 0

while True:
	idade = int(input('IDADE: '))

	while True:
		sexo = str(input('SEXO: [ M / F ]')).strip().upper()[0]
		print('-=' * 20)

		if sexo != 'F' and sexo != 'M':
			print('SEXO INVÁLIDO! TENTE NOVAMENTE.')
			print('-=' * 20)
		else:
			break

	continuar = str(input('QUER CONTINUAR? [ S / N ]')).strip().upper()[0]
	
	if sexo == 'F' and idade < 20:
		mulhermenos20 += 1

	if sexo == 'M':
		homens += 1

	if idade > 18:
		mais18 += 1

	if continuar != 'S':
		break

print(f'A QUANTIDADE DE PESSOAS QUE TEM MAIS DE 18 É {mais18}.')
print(f'A QUANTIDADE DE HOMENS CADASTROS É {homens}.')
print(f'A QUANTIDADE DE MULHERES COM MENOS DE 20 É {mulhermenos20}.')
print('-=' * 20)
input('pressione ENTER para sair')
