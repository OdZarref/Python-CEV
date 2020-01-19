#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def calcula_fatorial(numero, show=False):
    """
    numero: Recebe o número do qual o usuário quer o fatorial.
    show: Recebe "True" para mostrar o processo fatorial ou "False" para não mostrar.
    return: Retorna o fatorial de "numero".
    """

    fatorial = 1

    if show == False:
        for contador in range (numero , 0, -1):
            fatorial *= contador
    else:
        for contador in range (numero , 0, -1):
            fatorial *= contador

            if contador == 1:
                print(f'{contador} = {fatorial}')
            else:
                print(f'{contador} x ', end='') 


calcula_fatorial(5, True)
help(calcula_fatorial)
