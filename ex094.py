#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade do grupo C) Uma lista com todas as mulheres. D) Uma lista com todos as pessoas com idade acima da média.

dados_pessoas = list()
continuar = ''
total_idade = total_mulheres = contador = 0

while True:
    print(f'{"CADASTRO DE PESSOAS":=^29}')
    dado_pessoa = dict()
    dado_pessoa['nome'] = str(input('Nome: ')).strip()

    while True:
        dado_pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]

        if dado_pessoa['sexo'] == 'F':
            total_mulheres += 1

        if dado_pessoa['sexo'] == 'F' or dado_pessoa['sexo'] == 'M':
            break
        else:
            print('=' * 14)
            print('SEXO INVÁLIDO!')
            print('=' * 14)

    dado_pessoa['idade'] = int(input('Idade: '))
    total_idade += dado_pessoa['idade']

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

        if continuar == 'S' or continuar == 'N':
            break
        else:
            print('=' * 15)
            print('OPÇÃO INVÁLIDA!')
            print('=' * 15)

    dados_pessoas.append(dado_pessoa)

    if continuar == 'N':
        break

    del dado_pessoa

idade_media = total_idade / len(dados_pessoas)

print('=' * 40)
print(f'Foram cadastradas {len(dados_pessoas)} pessoas')
print(f'A idade média é {idade_media:5.2f}')

if total_mulheres == 1:
    print('A única mulher cadastrada foi: ', end='')
    
    for elemento in dados_pessoas:
        if elemento['sexo'] == 'F':
            print(elemento['nome'])

elif total_mulheres > 1:
    print('As mulheres cadastradas foram: ', end='')

    for elemento in dados_pessoas:
        if elemento['sexo'] == 'F':
            contador += 1

            if contador == total_mulheres - 1:
                print(f'{elemento["nome"].upper()}, ', end='')
            else:
                print(elemento['nome'].upper())


print('Pessoas com idade acima da média: ')
for elemento in dados_pessoas:
    for chave, valor in elemento.items():
        if chave == 'idade' and valor > idade_media:
            print(f'\tNome = {elemento["nome"].upper()}', end='')
            print(f'; Sexo = {elemento["sexo"]}', end='')
            print(f'; Idade = {elemento["idade"]}')
print('=' * 40)
input('pressione ENTER para sair')