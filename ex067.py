#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
print('-=' * 20)
print('DIGITE UM NÚMERO E VEJA SUA TABUADA')

while True:
	print('-=' * 20)
	numero = int(input('>>>'))
	print('-=' * 20)
	
	if numero < 0:
		break

	for tabuada in range(1, 11):
		print(f'{numero} x {tabuada:>2} = {numero * tabuada}')

print('-=' * 20)
input('pressione ENTER para sair')