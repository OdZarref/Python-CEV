#Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar, para cada palavra,  quais são suas vogais.
tupla = ('palavra', 'feijao', 'natação', 'esporte', 'vaca', 'cachorro', 'miojo', 'conectado', 'fio', 'internet', 'seguro', 'carro', 'moto')

for palavra in tupla:
	print(f'{palavra.upper()} tem as vogais: ', end='')

	for letra in palavra:
		if letra in 'aeiou':
			print(letra, end='')

	print('')

print('=' * 29)
input('pressione ENTER para sair')