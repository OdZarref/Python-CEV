#Modifique as funções que fora criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por eleas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
def moeda(preco):
    return f'{preco:.2f}'.replace('.', ',')


def aumentar(preco, porcentagem, formatar):
    total = (preco / 100 * porcentagem) + preco

    if formatar == True:
        return moeda(total)
    else:
        return total


def diminuir(preco, porcentagem, formatar):
    total = preco - (preco / 100 * porcentagem)

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
        