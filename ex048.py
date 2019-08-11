#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 que se encontram no intervalo de 1 até 500.
s = 0
for c in range(1, 500, 2):
	if c % 3 == 0:
		s += c
print(f'A soma de todos os números ímpares múltiplos de 3 é {s}.')
print('-=' * 27)
input('pressione ENTER para sair')