#ex016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. Ex: Digite um número: 6.127 O número 6.127 tem a parte Inteira 6.
import math
print('DIGITE UM NÚMERO E VEJA SUA PORÇÃO INTEIRA')
num = float(input(': '))
print(f'A sua porção inteira é {math.floor(num)}')
print('-=' * 10)
input('pressione enter para sair')
