#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Ex: Após a sopa
print('-=' * 28)
print('DIGITE ALGO E VEJA SE É UM PALÍNDROMO! (sem acentuações)')

print('-=' * 28)
junto = ''
contrario = ''
frase = str(input(':')).strip().upper().split()
junto = ''.join(frase)

for letra in range(len(junto) - 1, -1, -1):
	contrario += junto[letra]
print(f'{junto} ao contrário é {contrario}.')

if contrario == junto:
	print('TEMOS UM PALÍNDROMO!')
else:
	print('NÃO TEMOS UM PALÍNDROMO.')

print('-=' * 20)
input('pressione ENTER para sair')