def aumentar(preco, porcentagem):
    total = (preco / 100 * porcentagem) + preco
    return total


def diminuir(preco, porcentagem):
    total = preco - (preco / 100 * porcentagem)
    return total


def metade(preco):
    total = preco / 2
    return total


def dobro(preco):
    total = preco * 2
    return total