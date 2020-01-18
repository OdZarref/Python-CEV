#Faça um programa que tenha um função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada: A)De 1 até 10 de 1 em 1 B)De 10 até 0, de 2 em 2 C) Uma contagem personalizada
from time import sleep


def conte(inicio, fim, passo):
    contador = 0

    if passo < 0:
        while True:
            passo += 1
            contador += 1

            if passo == 0:
                passo += contador
                break

    elif passo == 0:
        passo = 1

    print('=' * 36)
    print(f'Contagem do {inicio} até {fim} ao passo de {passo}:', flush=True)

    if inicio > fim:
        while inicio >= fim:
            if inicio < fim + passo:
                print(inicio, flush=(True))
                inicio -= passo
                sleep(0.2)
            else:
                print(inicio, end=' > ', flush=(True))
                inicio -= passo
                sleep(0.2)

    
    elif inicio < fim:
        while inicio <= fim:
            if inicio > fim - passo:
                print(inicio, flush=(True))
                inicio += passo
                sleep(0.2)
            else:
                print(inicio, end=' > ', flush=(True))
                inicio += passo
                sleep(0.2)


conte(1, 10, 1)
conte(10, 0, 2)

print('=' * 36)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
conte(inicio, fim, passo)

print('=' * 36)
input('pressione ENTER para sair')
