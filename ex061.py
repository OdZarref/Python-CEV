#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
termo = int(input('TERMO: '))
razao = int(input('RAZÃO: '))
contador = 10
print('-=' * 20)

while contador > 0:

	if contador > 1:
		print(f'{termo} > ', end='')
	else:
		print(termo)
	termo += razao
	contador -= 1

print('-=' * 20)
input('pressione ENTER para sair')