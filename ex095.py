#Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
print(f'{"==ANÁLISE DE DESEMPENHO=="}')
todos_jogadores = list()
continuar = ''
opcao = 0

while True:
    continuar = ''
    dados_jogador = dict()
    gols_partidas = list()
    dados_jogador['nome'] = str(input('Nome: ')).strip()
    partidas_jogadas = int(input('Quantas partidas? '))
    total_gols = 0

    for contador in range(0, partidas_jogadas):
        gols_partidas.append(int(input(f'Gols na {contador + 1}° partida: ')))
        total_gols += gols_partidas[contador]

    dados_jogador['gols'] = gols_partidas
    dados_jogador['total de gols'] = total_gols
    todos_jogadores.append(dados_jogador.copy())
    dados_jogador.clear()

    while True:
        continuar = str(input('Continuar? [S/N]')).strip().upper()[0]

        if continuar == 'N' or continuar == 'S':
            break
        else:
            print('=' * 14)
            print('OPÇÃO INVÁLIDA')
            print('=' * 14)

    if continuar == 'N':
        break


print('=' * 41)
print(f'|cod={"Nome":=<15}{"Gols":=<15}{"Total":=<5}|')

for posicao, elemento in enumerate(todos_jogadores):
    print(f'|{posicao + 1} = ', end='')

    for chave, valor in elemento.items():
        if chave == 'total de gols':
            print(f'{str(valor):^5}', end='')
        else:
            print(f'{str(valor):<15}', end='')
    
    print('|')
print('=' * 41)


while opcao != 999:
    while True:
        opcao = int(input('Selecione cod. do jogador: [999 p/ sair]'))

        if opcao > len(todos_jogadores) and opcao != 999:
            print('=' * 14)
            print('OPÇÃO INVÁLIDA!')
            print('=' * 14)

        elif opcao < 1:
            print('=' * 14)
            print('OPÇÃO INVÁLIDA!')
            print('=' * 14)

        else:
            break

    for posicao, elemento in enumerate(todos_jogadores):
        if posicao == opcao - 1:
            print('=' * 37)
            print(f'|{"Nome":=<15}{"Gols":=<15}{"Total":=<5}|')
            print('|', end='')

            for chave, valor in elemento.items():

                if chave == 'total de gols':
                    print(f'{str(valor):^5}', end='')
                else:
                    print(f'{str(valor):<15}', end='')
            
            print('|')
            
            contador = 0
            print('|-----------------------------------|')

            for chave, valor in elemento.items():
                if chave == 'gols':
                    for elemento in valor:
                        contador += 1
                        print(f'|      |Gols na {contador}° partida: {elemento}|', end='')
                        print(f'{"|":>7}')

            print('=' * 37)
print('=' * 43)  
input('pressione ENTER para sair')