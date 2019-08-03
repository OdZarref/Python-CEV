#ex002: Crie um script que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.
dia = str(input('Digite o seu dia de nascimento: '))
mes = str(input('Digite o seu mês de nascimento: '))
ano = str(input('Digite o seu ano de nascimento: '))
print(f'Você nasceu em {dia}/{mes}/{ano}, certo?')
print('-=' * 10)
input('pressione enter para sair')
