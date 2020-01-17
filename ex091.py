#Crie um programa onde quatro jogadores joguem um dado e tenham resultados aleatórios. Guarde todos esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado.
from random import randint
from operator import itemgetter

contador = 0
jogadores = {'jogador1': randint(0, 6), 'jogador2': randint(0, 6), 'jogador3': randint(0, 6), 'jogador4': randint(0, 6), }
colocacao = list()
colocacao = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for chave, valor in jogadores.items():
    print(f'{chave} = {valor}')

print(f'{"COLOCAÇÃO":=^29}')

for chave, valor in colocacao:
    contador += 1
    print(f'{contador}° lugar = {chave}, {valor} pontos')

print('=' * 29)
input('pressione ENTER para sair')