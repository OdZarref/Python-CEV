#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: -Até 9 anos: MIRIM. -Até 14 anos: INFANTIL. -Até 19 anos: JUNIOR. -Até 25 anos: SÊNIOR. -Acima: MASTER.
import datetime
nas = int(input('Ano de Nascimento: '))
atual = datetime.date.today().year
idade = atual - nas
print('-=' * 20)
if idade <= 9:
	print('CATEGORIA: MIRIM')
elif idade > 9 and idade < 15:
	print('CATEGORIA: INFANTIL')
elif idade > 14 and idade < 20:
	print('CATEGORIA: JUNIOR')
elif idade > 19 and idade < 26:
	print('CATEGORIA: SÊNIOR')
else:
	print('CATEGORIA: MASTER')
print('-=' * 20)
input('pressione ENTER para sair')
