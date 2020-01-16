#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [[], [], []]
dado_temporario = 0
print(f'{"MATRIZ":=^25}')

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f'Matriz [{linha}, {coluna}]: ')))

print('=' * (9 * 3))

for item in matriz:
    for numero in item:
        if numero == item[-1]:
            print(f'[{numero:^7}]')
        else:
            print(f'[{numero:^7}]', end='')

print('=' * (9 * 3))
input('pressione ENTER para sair')