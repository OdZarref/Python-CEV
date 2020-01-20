#Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheir() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.
from utilidadesCEV import moeda, dados

preco = dados.leia_dinheiro('Preço: ')
porcentagem_aumento = int(input('Porcentagem de aumento: '))
porcentagem_diminuicao = int(input('Porcentagem de diminuição: '))
formatar = str(input('Formatar? ')).upper()[0]
formatacao = False

if formatar == 'S':
    formatacao = True

moeda.resumo(preco, porcentagem_aumento, porcentagem_diminuicao, formatacao)