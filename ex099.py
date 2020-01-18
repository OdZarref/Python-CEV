#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint

def maior(*numeros):
    maior = 0

    for posicao, elemento in enumerate(numeros):
        if posicao == 0:
            maior = elemento
        else:
            if elemento > maior:
                maior = elemento

    print(f'Foram informados os valores ', end='')

    for elemento in numeros:
        if elemento == numeros[-1]:
            print(elemento, end='.')
        else:
            print(elemento, end=', ')

    print(f' No total são {len(numeros)}. E o maior é {maior}.')


maior(randint(1, 99), randint(1, 99), randint(1, 99), randint(1, 99))
maior(randint(1, 99), randint(1, 99), randint(1, 99), randint(1, 99), randint(1, 99), randint(1, 99))
maior(randint(1, 99), randint(1, 99), randint(1, 99), randint(1, 99), randint(1, 99), randint(1, 99), randint(1, 99), randint(1, 99))
maior(randint(1, 99), randint(1, 99))

print('=' * 67)
input('pressione ENTER para sair')
