#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
s = 0
for c in range(1, 7):
	num = int(input(f'{c}º NÚMERO: '))
	if num % 2 == 0:
		s += num
print(f'A soma dos números pares digitados é {s}')
print('-=' * 20)
input('pressione ENTER para sair')