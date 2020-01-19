#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex) n = leiaint("Digite um número: ")

def leia_numerico():
    """
    numero_lido: Recebe uma string.
    numero: Recebe o número inteiro de "numero_lido".
    return: Returna o uma mensagem com o número digitado.
    """
    while True:
        numero_lido = str(input('Número: '))

        if numero_lido.isnumeric() == True:
            numero = int(numero_lido)
            break
        else:
            print('\033[31mErro! Digite um número.\033[m')

    return f'\033[32mVocê digitou o número {numero}\033[m'

print(leia_numerico())