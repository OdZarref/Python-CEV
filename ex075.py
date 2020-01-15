#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posicação foi digitado o primeiro valor 3. C) Quais foram os números pares.
contador = segundo_contador = 0
valores = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print('=' * 44)
print(f'O valor NOVE apareceu por {valores.count(9)} vezes.')
print(f'O valor TRÊS apareceu primeiro na {valores.index(3) + 1} posição.')
print(f'Os valores pares são: ', end='')

for valor in valores:
	 print(f'{valor} > ', end='')

print('')
print('=' * 44)
input('pressione ENTER para sair')