def linhas(texto):
    print('=' * 30)
    print(texto.center(30))
    print('=' * 30)


def mostrar_opcoes(lista):
    contador = 0

    for item in lista:
        contador += 1
        print(f'{contador} - {item}')


def leia_inteiro(texto):
    while True:
        try:
            numero = int(input(texto))
        except (TypeError, ValueError, KeyboardInterrupt):
            print('\033[31mDigite uma opção válida!\033[m')
            continue
        else:
            return numero
