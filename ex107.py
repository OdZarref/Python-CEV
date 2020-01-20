#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import ex107moedas

preco = float(input('Preço: '))
porcentagem_aumento = int(input('Porcentagem de aumento: '))
porcentagem_diminuicao = int(input('Porcentagem de diminuição: '))

print(f'Com o aumento de {porcentagem_aumento}% o preço fica R${ex107moedas.aumentar(preco, porcentagem_aumento)}')
print(f'Com a diminuição de {porcentagem_diminuicao}% o preço fica R${ex107moedas.diminuir(preco, porcentagem_diminuicao)}')
print(f'A metade é R${ex107moedas.metade(preco)}')
print(f'O dobro é R${ex107moedas.dobro(preco)}')