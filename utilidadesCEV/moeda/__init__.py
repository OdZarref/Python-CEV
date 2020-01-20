def moeda(preco):
    return f'{preco:.2f}'


def aumentar(preco, porcentagem_aumento, formatar):
    total = (preco / 100 * porcentagem_aumento) + preco

    if formatar == True:
        return moeda(total)
    else:
        return total


def diminuir(preco, porcentagem_aumento, formatar):
    total = preco - (preco / 100 * porcentagem_aumento)

    if formatar == True:
        return moeda(total)
    else:
        return total


def metade(preco, formatar):
    total = preco / 2

    if formatar == True:
        return moeda(total)
    else:
        return total


def dobro(preco, formatar):
    total = preco * 2

    if formatar == True:
        return moeda(total)
    else:
        return total


def resumo(preco, porcentagem_aumento, porcentagem_diminuicao, formatar):
    print('=' * 32)
    print('RESUMO'.center(32))
    print('=' * 32)
    print(f'PREÇO ANALISADO: \tR${moeda(preco)}')
    print(f'{porcentagem_aumento}% DE AUMENTO: \tR${aumentar(preco, porcentagem_aumento, formatar)}')
    print(f'{porcentagem_diminuicao}% DE DIMINUIÇÃO: \tR${diminuir(preco, porcentagem_diminuicao, formatar)}')
    print(f'METADE DO PREÇO: \tR${metade(preco, formatar)}')
    print(f'DOBRO DO PREÇO: \tR${dobro(preco, formatar)}')
    print('=' * 32)
