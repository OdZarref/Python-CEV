def moeda(preco):
    return f'{preco:<5.2f}'.replace('.', ',')


def aumentar(preco, porcentagem):
    total = (preco / 100 * porcentagem) + preco
    return moeda(total)


def diminuir(preco, porcentagem):
    total = preco - (preco / 100 * porcentagem)
    return moeda(total)


def metade(preco=0):
    total = preco / 2
    return moeda(total)


def dobro(preco=0):
    total = preco * 2
    return moeda(total)