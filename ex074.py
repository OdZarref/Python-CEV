#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois, disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
contador = maior = menor = 0
numero_aleatorio = randint(0, 11)
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

for numero in tupla:
	contador += 1
	
	if contador != 5:
		print(f'{numero} > ', end='')
	else:
		print(numero)

	if contador == 1:
		maior = numero
		menor = numero
	else:
		if numero > maior:
			maior = numero

		if numero < menor:
			menor = numero

print('=' * (26 + len(str(maior))))
print(f'O maior valor gerado foi: {maior}')
print(f'O menor valor gerado foi: {menor}')
print('=' * (26 + len(str(maior))))
input('pressione ENTER para sair')