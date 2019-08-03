#ex010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$ 1,00 = R$ 3,27.'''
print('CONVERSOR DE REAL PARA DOLAR\nDOLAR = 3.27')
print('')
reais = float(input('REAL: '))
print('É possível comprar {} dólares.'.format(reais / 3.27))
pprint('-=' * 10)
input('pressione ENTER para sair')
