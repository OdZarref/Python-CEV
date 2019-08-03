#ex015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.
print('DIGITE AS INFORMAÇÕES O VEJA O TOTAL A PAGAR.')
km = int(input('KILOMETROS: '))
dias = int(input('DIAS: '))
print(f'O PREÇO TOTAL A PAGAR É {km * 0.15 + dias * 60} R$.')
print('-=' * 10)
input('pressione enter para sair')
