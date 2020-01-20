#Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
from utilidadesCEV import moeda

preco = float(input('Preço: '))
porcentagem_aumento = int(input('Porcentagem de aumento: '))
porcentagem_diminuicao = int(input('Porcentagem de diminuição: '))
formatar = str(input('Formatar? ')).upper()[0]
formatacao = False

if formatar == 'S':
    formatacao = True

moeda.resumo(preco, porcentagem_aumento, porcentagem_diminuicao, formatacao)