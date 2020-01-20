#Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
import ex110moedas

preco = float(input('Preço: '))
porcentagem_aumento = int(input('Porcentagem de aumento: '))
porcentagem_diminuicao = int(input('Porcentagem de diminuição: '))
formatar = str(input('Formatar? ')).upper()[0]
formatacao = False

if formatar == 'S':
    formatacao = True


ex110moedas.resumo(preco, porcentagem_aumento, porcentagem_diminuicao, formatacao)