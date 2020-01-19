#Faça um mini-sistema que utilize o Interactive Help do python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra "FIM", o programa se encerrará. OBS: use cores
from time import sleep

c = (
'\033[m',
'\033[0;30;41m', 
'\033[0;30;42m', 
'\033[0;30;43m', 
'\033[0;30;44m', 
'\033[0;30;45m', 
'\033[7;30m'
)


def ajuda(com):
    titulo(f'Procurando o manual da função \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('=' * tam)
    print(msg)
    print('=' * tam)
    print(c[0], end='')
    sleep(1)



while True:
    titulo('MODO DE AJUDA INTERATIVO', 2)
    comando = str(input('Função > '))
    
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('Fim do programa.', 1)

