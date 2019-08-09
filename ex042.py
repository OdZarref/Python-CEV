#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostar que tipo de triângulo será formado: -Equilátero: Todos os lados iguais. -Isósceles: Dois lados iguais. -Escaleno: Todos os lados diferentes.
re1 = float(input('Reta 1: '))
re2 = float(input('Reta 2: '))
re3 = float(input('Reta 3: '))
print('-=' * 20)
if re1 < re2 + re3 and re2 < re1 + re3 and re3 < re1 + re2:
	if re1 == re2 and re2 == re3:
		print('É POSSÍVEL FORMAR UM TRIÂNGULO EQUILÁTERO.')
	elif re1 == re2 and re2 != re3 or re2 == re3 and re3 != re1 or re3 == re1 and re1 != re2:
		print('É POSSÍVEL FORMAR UM TRIÂNGULO ISÓSCELES.')
	else:
		print('É POSSÍVEL FORMAR UM TRIÂNGULO ESCALENO')
else:
	print('NÃO É POSSÍVEL FORMAR UM TRIÂNGULO.')
print('-=' * 20)
input('pressione ENTER para sair')
