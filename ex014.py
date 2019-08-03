#ex014: Escreva um programa que converta um a temperatura digitada em ºC e converta para ºF.
print('CONVERSOR DE CELSIUS PARA FAHRENHEIT')
celsius = int(input('CELSIUS:'))
print('{}ºF'.format(celsius / 5 * 9 + 32))
print('-=' * 10)
input('pressione enter para sair')
