#Modifique as funções que fora criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por eleas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import ex109moedas

preco = float(input('Preço: '))
porcentagem_aumento = int(input('Porcentagem de aumento: '))
porcentagem_diminuicao = int(input('Porcentagem de diminuição: '))

print('=' * 40)
print(f'Com o aumento de {porcentagem_aumento}% o preço fica R$ {ex109moedas.aumentar(preco, porcentagem_aumento, formatar=True)}.')
print(f'Com a diminuição de {porcentagem_diminuicao}% o preço fica R$ {ex109moedas.diminuir(preco, porcentagem_diminuicao, formatar=True)}.')
print(f'A metade é R${ex109moedas.metade(preco, formatar=True)}.')
print(f'O dobro é R${ex109moedas.dobro(preco, formatar=True)}.')
print('=' * 40)

input('pressione ENTER para sair')