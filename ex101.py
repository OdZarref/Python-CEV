#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.


def voto(ano_nascimento):
    from datetime import date

    ano_atual = date.today().year

    if (ano_atual - ano_nascimento) < 16:
        return f'Com {ano_atual - ano_nascimento} anos, não Vota.'

    elif (ano_atual - ano_nascimento) >= 16 < 18 or (ano_atual - ano_nascimento) >= 65:
        return f'Com {ano_atual - ano_nascimento} anos, O voto é opcional.'

    else:
        return f'Com {ano_atual - ano_nascimento} anos, o voto é obrigatório.'


ano_nascimento = int(input('Ano de nascimento: '))
print('=' * 25)
print(voto(ano_nascimento))
print('=' * 25)
input('pressione ENTER para sair')