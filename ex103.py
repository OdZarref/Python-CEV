#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um nome_jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do nome_jogador, mesmo que algum dado não tenha sido informado corretamente.


def cadastra_jogador(nome_jogador, gols=0):
    """
    nome_jogador: Recebe o nome do jogador.
    gols: Recebe a quantidade de gols do jogador.
    return: Retorna o nome (caso inserido) e o número de gols (caso inserido).
    """
    return f'O nome_jogador {nome_jogador} fez {gols} gols'


nome_jogador = str(input('Nome: '))
gols = str(input('Gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome_jogador.strip() == '':
    nome_jogador = '<desconhecido>'

print(cadastra_jogador(nome_jogador, gols))
