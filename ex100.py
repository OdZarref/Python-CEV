#Faça um programa que tenha uma lista chamada "numeros" e duas funções chamadas sorteia() e soma_par(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint


def sorteia():
    contador = 0

    while contador != 5:
        numeros.append(randint(1, 99))
        contador += 1

    print(f'Foram sorteados os números: ', end='')

    for elemento in numeros:
        if elemento == numeros[-1]:
            print(f'{elemento}.')
        else:
            print(f'{elemento}, ', end='')


def soma_pares(lista):
    soma = 0

    for elemento in lista:
        if elemento % 2 == 0:
            soma += elemento
    
    print(f'A soma de todos os pares é. {soma}')


numeros = list()
sorteia()
soma_pares(numeros)

print('=' * 31)
input('pressione ENTER para sair')
