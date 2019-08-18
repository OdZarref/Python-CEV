#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou náo continuar a digitar valores.
resposta = 'S'
contador = somador = 0

while resposta in 'S':
	contador += 1
	numero = int(input('DIGITE UM NÚMERO>>>'))

	if contador == 1:
		maior = menor = numero
	else:
		if numero > maior:
			maior = numero
		if numero < menor:
			menor = numero

	somador += numero
	resposta = str(input('VOCÊ QUER CONTINUAR? [S/N]')).strip().upper()
	print('-=' * 17)

print(f'O MAIOR NÚMERO DIGITADO FOI {maior}.')
print(f'O MENOR NÚMERO DIGITADO FOI {menor}.')
print(f'A MÉDIA É {somador / contador}')
print('-=' * 17)
input('pressione ENTER para sair')