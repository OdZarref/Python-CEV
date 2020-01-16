#Aprimore o desafio anterior, mostrando no final. A) A soma de todos os valores pares digitados. B)A soma dos valores da terceira coluna. C) O maior valor da segunda linha.
matriz = [[], [], []]
dado_temporario = soma_pares = maior_segunda_linha = soma_terceira_coluna = contador = 0
print(f'{"MATRIZ":=^25}')

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f'Matriz [{linha}, {coluna}]: ')))

print('=' * (9 * 3))

for item in matriz:
    for numero in item:
        contador += 1
        if numero % 2 == 0:
            soma_pares += numero

        if contador % 3 == 0:
            soma_terceira_coluna += numero

        if contador > 3 and contador < 7:
            if numero == 0:
                maior_segunda_linha = numero
            else:
                if numero > maior_segunda_linha:
                    maior_segunda_linha = numero

        if numero == item[-1]:
            print(f'[{numero:^7}]')
        else:
            print(f'[{numero:^7}]', end='')

print('=' * (9 * 3))

print(f'Soma dos pares: {soma_pares}')
print(f'Soma dos itens da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior número da segunda linha é: {maior_segunda_linha}')
print(f'=' * (35 + len(str(maior_segunda_linha))))
input('pressione ENTER para sair')