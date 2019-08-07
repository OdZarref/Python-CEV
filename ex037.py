#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual o será a base de conversão: -"1" para binário. -"2" para octal. -"3" para hexadecimal.
num = int(input('Digite um número inteiro: ')) #número
print('-=' * 20)
print("""Escolha uma das bases para conversão:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL""")
es = int(input(': '))
print('-=' * 20)
if es == 1:
	print(f'r: {bin(num)[2:]}')
elif es == 2:
	print(f'r: {oct(num)[2:]}')
elif es == 3:
	print(f'r: {hex(num)[2:]}')
else:
	print('OPÇÃO INVÁLIDA')
print('-=' * 20)
input('pressione ENTER para sair')