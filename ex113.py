#Reescreva função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leia_inteiro():
    while True:
        try:
            numero = int(input('Digite um número inteiro: '))
        except (TypeError, ValueError):
            print('\033[31mDIGITE UM VALOR NUMÉRICO INTEIRO!\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuário não digitou nenhum número. Variável recebe "0"')
            return 0
        else:
            return numero


def leia_flutuante():
    while True:
        try:
            numero = float(input('Digite um número flutuante: '))
        except (TypeError, ValueError):
            print('\033[31mDIGITE UM VALOR NUMÉRICO FLUTUANTE!\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuário não digitou nenhum número. Variável recebe "0"')
            return 0
        else:
            return numero


valor_inteiro = leia_inteiro()
valor_flutuante = leia_flutuante()
print(f'O valor INTEIRO digitado foi {valor_inteiro}. E o valor FLUTUANTE foi {valor_flutuante}.')