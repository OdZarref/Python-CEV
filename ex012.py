#ex012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
print('DIGITE UM PREÇO E VEJA-O COM DESCONTO DE 5%.')
preco = float(input(': '))
print('Com desconto de 5% o preço fica: {} R$.'.format(preco / 100 * 95))
print('-=' * 10)
input('pressione ENTER para sair')
