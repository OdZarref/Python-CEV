#ex:017: Faça um programa que leia o ca soma domprimento do cateto oposto e do cateto adjacente de um triângulo, calcule o mostre o comprimento da hipotenusa.
co = float(input('Cumprimento do Cateto Oposto: '))
ca = float(input('Cumprimento do Cateto Adjacente: '))
print(f'A hipotenusa é {(co ** 2 + ca ** 2) ** (1 / 2)}')
print('-=' * 10)
input('pressione ENTER para sair')
