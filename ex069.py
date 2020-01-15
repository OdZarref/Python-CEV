#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastranda, o programa deverá perguntar se o usuário quer ou não continuarç. No final, mostre: A) Quantas pessoas tem mais de 18 anos. B) Quantos homens foram cadastrados. C) Quantas mulheres tem menos de 20 anos.
quantos_mais_dezoito = quantos_homens = mulheres_menos_vinte = 0

while True:
	 continuar = sexo = ''
	 idade = int(input('Idade: '))

	 while 'M' not in sexo and 'F' not in sexo:
		 sexo = str(input('Sexo: [M/F]')).upper()[0]

	 if idade > 18:
	 	quantos_mais_dezoito += 1

	 if 'M' in sexo:
	 	quantos_homens += 1

	 if 'F' in sexo and idade < 20:
	 	mulheres_menos_vinte += 1

	 while 'S' not in continuar and 'N' not in continuar:
		 continuar = str(input('Continuar? [S/N] ')).upper()[0]

	 if 'N' in continuar:
	 	break

	 print('=' * 16)

print('=' * (33 + len(str(mulheres_menos_vinte))))
print(f'{"PROGRAMA FINALIZADO":^33}')
print('=' * (33 + len(str(mulheres_menos_vinte))))
print(f'Total de pessoas maiores de 18: {quantos_mais_dezoito}')
print(f'Total de homens cadastrados: {quantos_homens}')
print(f'Total de mulheres menores de 20: {mulheres_menos_vinte}')
print('=' * (33 + len(str(mulheres_menos_vinte))))
input('pressione ENTER para sair')