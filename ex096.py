#Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retângular (largura e comprimento) e mostre a área do terreno.
def calcule_area(largura, comprimento):
    print(f'A área deste terreno é de {largura * comprimento}m²')


largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
calcule_area(largura, comprimento)
input('pressione ENTER para sair')
