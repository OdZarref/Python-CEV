#Crie um tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: A) Apenas os 5 primeiros colocados. B) Os últimos 4 colocados da tabela. C) Uma lista com os times em ordem alfabética. D) Em que posição na tabela está o time da Chapecoense.
colocacao_brasileirao = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Curitiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'{"TABELA BRASILEIRÃO":=^94}')
print('=' * 94)
print(f'Os CINCO primeiros colocados são: {colocacao_brasileirao[0:5]}')
print('=' * 94)
print(f'Os QUATRO últimos colocados são: {colocacao_brasileirao[16:]}')
print('=' * 94)
print(f'Os times em ordem alfabética: {sorted(colocacao_brasileirao)}')
print('=' * 94)
print(f'O Chapecoense está na {colocacao_brasileirao.index("Chapecoense") + 1} colocação')
print('=' * 94)
input('pressione ENTER para sair')