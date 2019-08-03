#ex018: Faça um programa que leia um ângulo qualquer a mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
a = float(input('Ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print(f'Este ângulo tem o seno de {s}, o cosseno de {c} e a tangente de {t}')
print('-=' * 10)
input('pressione enter para sair')
