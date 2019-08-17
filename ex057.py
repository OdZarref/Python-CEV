#Faça um programa que leio o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('QUAL O SEU SEXO? [ M / F ] ')).strip().upper()[0]
print('-=' * 21)

while sexo not in 'MF':
	print('OPÇÃO INVÁLIDA!')
	sexo = str(input('QUAL O SEU SEXO? [ M / F ] ')).strip().upper()[0]

if sexo == 'M':
	print('Você foi registrado como do sexo MASCULINO.')
elif sexo == 'F':
	print('VOCÊ FOI REGISTRADO COMO DO SEXO FEMININO.')

print('-=' * 21)
input('pressione ENTER para sair')