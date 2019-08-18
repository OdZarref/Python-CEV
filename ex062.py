#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disse que quer mostrar 0 termos.
termo = int(input('TERMO: '))
razao = int(input('RAZÃO: '))
contador = 0
termos = 0
mais = 10
print('-=' * 20)

while mais != 0:
	contador = 0

	while contador != mais:
		termos += mais

		if contador < mais - 1:
			print(f'{termo} > ', end='')
		else:
			print(termo)
		contador += 1
		termo += razao

	print('-=' * 20)
	mais = int(input('QUANTOS TERMOS QUER MOSTRAR A MAIS? '))

	if mais != 0:
		print('-=' * 20)

print('-=' * 20)
input('pressione ENTER para sair')
