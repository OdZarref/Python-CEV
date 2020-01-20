def leia_dinheiro(preco):
    numero = ''

    while True:
        numero = str(input('Preço: ')).replace(',', '.').strip()

        if numero.isalpha() or numero == '':
            print('\033[31mDIGITE UM VALOR NÚMERICO.\033[m')
        else:
            numero = float(numero)
            break

    return numero