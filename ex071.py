#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print(f'{"BANCO QUE NUNCA FUNCIONA":=^31}')
cinquenta = vinte = dez = um = 0
valor_saque = float(input('DIGITE O VALOR DE SAQUE: '))

while valor_saque >= 50:
	valor_saque	-= 50
	cinquenta += 1

while valor_saque >= 20:
	valor_saque -= 20
	vinte += 1

while valor_saque >= 10:
	valor_saque -= 10
	dez += 1

while valor_saque >= 1:
	valor_saque -= 1
	um += 1

print(f'{cinquenta} NOTAS DE CINQUENTA')
print(f'{vinte} NOTAS DE VINTE')
print(f'{dez} NOTAS DE DEZ')
print(f'{um} NOTAS DE UM')
print('=' * 31)
input('pressione ENTER tecla para sair')