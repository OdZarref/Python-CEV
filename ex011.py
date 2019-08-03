#ex011: Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tintas necessárias para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
altura = float(input('ALTURA: '))
largura = float(input('LARGURA: '))
area = altura * largura
print(f'Será necessário {area / 2} litros de tinta.')
print('-=' * 10)
input('pressione ENTER para sair')
