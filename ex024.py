#ex024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome ‘SANTO’
city = str(input('Digite o nome de uma cidade: ')).strip().upper().split()
r = 'SANTO' in city[0]
print(r)
print('-=' * 10)
input('pressione ENTER para sair')