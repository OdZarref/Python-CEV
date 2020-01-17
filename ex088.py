#Faça um programa que ajuda um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

print(f'{"GERADOR DE PALPITES":=^35}')
quantos_jogos = int(input('Quantos palpites? '))
jogos = list()
jogo_gerado = list()

for contador in range(0, quantos_jogos):
    while True:
        dado = randint(1, 60)
        
        if dado not in jogo_gerado:
            jogo_gerado.append(dado)
        
        if len(jogo_gerado) == 6:
            break
    
    jogo_gerado.sort()
    jogos.append(jogo_gerado[:])
    jogo_gerado.clear()

print(f'{"PALPITES GERADOS":=^35}')

for contador, jogo in enumerate(jogos):
    print(f'Palpite {contador + 1}: {jogo}')

print(f'=' * 35)
input('pressione ENTER para sair')
