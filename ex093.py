#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
print(f'{"==ANÁLISE DE DESEMPENHO=="}')
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

print('=' * 25)

for chave, valor in dados_jogador.items():
    print(f'{chave.upper()} = {valor}')

print('=' * 25)
input('pressione ENTER para sair')