#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date

print(f'{"CADASTRO TRABALHADOR":=^28}')
dados = dict()
dados['nome'] = str(input('Nome: ')).strip()
dados['ano de nascimento'] = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - dados['ano de nascimento']
dados['carteira de trabalho'] = int(input('Carteira de trabalho: [0 p/ não tem] '))

if dados['carteira de trabalho'] != 0:
    dados['ano de contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['idade de aposentadoria'] = dados['ano de contratação'] - dados['ano de nascimento'] + 35

print('=' * 27)

for chave, valor in dados.items():
    if chave == 'salário':
        print(f'{chave.upper()} = R${valor}')
    else:
        print(f'{chave.upper()} = {valor}')

print('=' * 27)
input('pressine ENTER para sair')